Personal Finance Tracker - Complete Project Structure
Project Directory Structure

<img width="515" height="497" alt="image" src="https://github.com/user-attachments/assets/4bd132b5-af19-4198-9983-9c6c46836f17" />



🛠️ Technology Stack
Backend
Flask - Lightweight Python web framework
SQLAlchemy - Database ORM
SQLite - Local database storage
WTForms - Form handling and validation

Frontend

Bootstrap 5 - Responsive CSS framework

https://github.com/user-attachments/assets/ee7472ba-acc0-4743-b3e4-58ac674e1bb4


Chart.js - Interactive data visualizations
Font Awesome - Icon library
Custom CSS - Professional styling

📱 Screenshots
Dashboard Overview
The main dashboard provides a comprehensive view of your financial status with interactive charts and recent activity.
Transaction Management
Easily add, view, and manage all your financial transactions with intuitive forms and pagination.
Category Management
Create custom categories with color coding for better organization and visual appeal.
Financial Reports
Generate detailed reports with charts showing spending trends and financial insights.
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/83f10d74-a353-42e2-8369-f5e6f6817014" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/d710f872-f1ad-4046-a840-6d41808a1df6" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/004acf2e-339e-4ae9-a060-adfecb539384" />
<img width="596" height="406" alt="image" src="https://github.com/user-attachments/assets/0eb565be-0613-49bc-bdf7-30b71916d81f" />





Environment Variables
Create a .env file in the root directory for production settings:
envSECRET_KEY=your-super-secret-key-here
DATABASE_URL=sqlite:///finance.db
FLASK_ENV=production
Database Configuration
The application uses SQLite by default. For production, you can configure PostgreSQL or MySQL:
python# config.py
SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/finance_db'
🚀 Deployment
Heroku Deployment

Create Procfile
web: python app.py

Deploy to Heroku
bashgit add .
git commit -m "Initial commit"
heroku create your-app-name
git push heroku main


Railway Deployment

Connect your GitHub repository to Railway
Configure environment variables
Deploy automatically

PythonAnywhere Deployment

Upload files to your PythonAnywhere account
Create a web app with Flask
Configure WSGI file

DigitalOcean/AWS/GCP

Set up a virtual server
Install dependencies
Configure gunicorn and nginx
Set up SSL certificate

🔒 Security Features

CSRF Protection - Forms protected against cross-site request forgery
Input Validation - Server-side validation for all user inputs
SQL Injection Prevention - SQLAlchemy ORM prevents SQL injection
Session Management - Secure session handling
Environment Variables - Sensitive data stored in environment variables

📊 Default Categories
The application comes with pre-configured categories:
CategoryColorTypeFood & DiningRedExpenseTransportationTealExpenseShoppingBlueExpenseEntertainmentYellowExpenseBills & UtilitiesPurpleExpenseHealthcarePinkExpenseSalaryGreenIncomeFreelanceOrangeIncomeInvestmentsBrownIncomeOtherGrayBoth
<img width="569" height="377" alt="image" src="https://github.com/user-attachments/assets/015de6be-7e36-4070-bee4-403a81a72a1d" />


🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

Development Guidelines

Follow PEP 8 style guide for Python code
Add comments for complex logic
Include tests for new features
Update documentation as needed

🐛 Bug Reports
If you find a bug, please create an issue with:

Detailed description of the problem
Steps to reproduce
Expected vs actual behavior
Screenshots (if applicable)
Environment details (OS, Python version, etc.)

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
MIT License

Copyright (c) 2025 Personal Finance Tracker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
🔮 Future Enhancements

 Multi-user support with authentication
 Budget planning and tracking
 Recurring transaction automation
 Data import/export (CSV, Excel)
 Mobile app development
 Bank integration APIs
 Advanced reporting with PDF export
 Goal setting and progress tracking
 Email notifications for spending alerts
 Multi-currency support


🙏 Acknowledgments

Flask - The Python web framework
Bootstrap - CSS framework
Chart.js - Chart library
Font Awesome - Icon library
SQLAlchemy - Database ORM

⭐ Show Your Support
If this project helped you, please consider giving it a star! ⭐

Built with ❤️ for personal finance management
