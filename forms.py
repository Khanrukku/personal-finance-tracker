from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, DateField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
from datetime import date

class TransactionForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0.01)])
    transaction_type = SelectField('Type', choices=[('income', 'Income'), ('expense', 'Expense')], validators=[DataRequired()])
    category_id = SelectField('Category', coerce=int, validators=[DataRequired()])
    date = DateField('Date', default=date.today(), validators=[DataRequired()])

class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired()])
    color = StringField('Color', default='#007bff')
