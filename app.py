from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from models import db, Transaction, Category
from forms import TransactionForm, CategoryForm
from config import Config
from datetime import datetime, timedelta
from sqlalchemy import func, extract
import calendar

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def create_tables():
    """Initialize database tables and create default categories"""
    with app.app_context():
        db.create_all()
        
        # Create default categories if none exist
        if Category.query.count() == 0:
            default_categories = [
                {'name': 'Food & Dining', 'color': '#ff6b6b'},
                {'name': 'Transportation', 'color': '#4ecdc4'},
                {'name': 'Shopping', 'color': '#45b7d1'},
                {'name': 'Entertainment', 'color': '#f9ca24'},
                {'name': 'Bills & Utilities', 'color': '#6c5ce7'},
                {'name': 'Healthcare', 'color': '#fd79a8'},
                {'name': 'Salary', 'color': '#00b894'},
                {'name': 'Freelance', 'color': '#fdcb6e'},
                {'name': 'Investments', 'color': '#e17055'},
                {'name': 'Other', 'color': '#636e72'}
            ]
            
            for cat_data in default_categories:
                category = Category(name=cat_data['name'], color=cat_data['color'])
                db.session.add(category)
            
            db.session.commit()

# Initialize database when app starts
create_tables()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # Get current month transactions
    current_month = datetime.now().month
    current_year = datetime.now().year
    
    # Calculate totals
    total_income = db.session.query(func.sum(Transaction.amount)).filter(
        Transaction.transaction_type == 'income',
        extract('month', Transaction.date) == current_month,
        extract('year', Transaction.date) == current_year
    ).scalar() or 0
    
    total_expenses = db.session.query(func.sum(Transaction.amount)).filter(
        Transaction.transaction_type == 'expense',
        extract('month', Transaction.date) == current_month,
        extract('year', Transaction.date) == current_year
    ).scalar() or 0
    
    balance = total_income - total_expenses
    
    # Get recent transactions
    recent_transactions = Transaction.query.order_by(Transaction.created_at.desc()).limit(5).all()
    
    # Get spending by category
    spending_by_category = db.session.query(
        Category.name,
        Category.color,
        func.sum(Transaction.amount).label('total')
    ).join(Transaction).filter(
        Transaction.transaction_type == 'expense',
        extract('month', Transaction.date) == current_month,
        extract('year', Transaction.date) == current_year
    ).group_by(Category.name, Category.color).all()
    
    return render_template('dashboard.html', 
                         total_income=total_income,
                         total_expenses=total_expenses,
                         balance=balance,
                         recent_transactions=recent_transactions,
                         spending_by_category=spending_by_category,
                         current_month=calendar.month_name[current_month])

@app.route('/transactions')
def transactions():
    page = request.args.get('page', 1, type=int)
    transactions = Transaction.query.order_by(Transaction.date.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    return render_template('transactions.html', transactions=transactions)

@app.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    form = TransactionForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]
    
    if form.validate_on_submit():
        transaction = Transaction(
            description=form.description.data,
            amount=form.amount.data,
            transaction_type=form.transaction_type.data,
            category_id=form.category_id.data,
            date=form.date.data
        )
        db.session.add(transaction)
        db.session.commit()
        flash('Transaction added successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('add_transaction.html', form=form)

@app.route('/categories')
def categories():
    categories = Category.query.all()
    form = CategoryForm()
    return render_template('categories.html', categories=categories, form=form)

@app.route('/add_category', methods=['POST'])
def add_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(
            name=form.name.data,
            color=form.color.data
        )
        db.session.add(category)
        db.session.commit()
        flash('Category added successfully!', 'success')
    return redirect(url_for('categories'))

@app.route('/reports')
def reports():
    # Get monthly spending trends
    monthly_data = db.session.query(
        extract('year', Transaction.date).label('year'),
        extract('month', Transaction.date).label('month'),
        func.sum(Transaction.amount).label('total'),
        Transaction.transaction_type
    ).group_by(
        extract('year', Transaction.date),
        extract('month', Transaction.date),
        Transaction.transaction_type
    ).order_by('year', 'month').all()
    
    return render_template('reports.html', monthly_data=monthly_data)

@app.route('/api/monthly_data')
def api_monthly_data():
    monthly_data = db.session.query(
        extract('year', Transaction.date).label('year'),
        extract('month', Transaction.date).label('month'),
        func.sum(Transaction.amount).label('total'),
        Transaction.transaction_type
    ).group_by(
        extract('year', Transaction.date),
        extract('month', Transaction.date),
        Transaction.transaction_type
    ).order_by('year', 'month').all()
    
    result = {}
    for item in monthly_data:
        key = f"{int(item.year)}-{int(item.month):02d}"
        if key not in result:
            result[key] = {'income': 0, 'expense': 0}
        result[key][item.transaction_type] = float(item.total)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
