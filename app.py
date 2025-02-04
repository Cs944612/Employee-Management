from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)

# Database setup (SQLite in memory or persistent .db file)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)  # Salary is now considered in Rupees

    def __repr__(self):
        return f"<Employee {self.name}>"

# Create the database (first time only)
with app.app_context():
    db.create_all()

# Home route - Display employees
@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

# Add employee route
@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    position = request.form['position']
    salary = float(request.form['salary'])  # Ensure input is converted to float (Rupees)

    new_employee = Employee(name=name, position=position, salary=salary)
    db.session.add(new_employee)
    db.session.commit()

    return redirect(url_for('index'))

# Edit employee route
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = Employee.query.get_or_404(id)

    if request.method == 'POST':
        employee.name = request.form['name']
        employee.position = request.form['position']
        employee.salary = float(request.form['salary'])  # Ensure input is stored correctly
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', employee=employee)

# Delete employee route
@app.route('/delete/<int:id>')
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()

    return redirect(url_for('index'))

# Run the app locally (on port 5000)
if __name__ == "__main__":
    app.run(port=5000, debug=False)
