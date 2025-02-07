# Employee Management System

A simple Flask-based web application for managing employee records. This project allows you to perform basic CRUD (Create, Read, Update, Delete) operations on employee data.

## Features

*** 1. View Employees:*** Display a list of all employees with their details (name, position, salary).
*** 2. Add Employees:*** Add new employees to the database.
*** 3. Edit Employees:*** Update existing employee details.
*** 4. Delete Employees:*** Remove employees from the database.
*** 5. Simple UI:*** Clean and user-friendly interface styled with CSS.


## Technologies Used

***Backend:*** Flask, SQLAlchemy
***Frontend:*** HTML, CSS
***Database:*** SQLite

## Prerequisites

- Python 3.x
- pip (Python package installer)


## Installation and Setup

1. Install Python on Windows

Follow these steps to install Python on Windows:

### Download Python:

- Go to the official Python website: python.org.
- Navigate to the Downloads section and download the latest version of Python for Windows.

### Run the Installer:

- Open the downloaded installer.
- Check the box that says "Add Python to PATH" at the bottom of the installer window.
- Click "Install Now" to proceed with the installation.

### Verify Installation:

- Open Command Prompt (Win + R, type cmd, and press Enter).
- Run the following command to check if Python is installed:
```
python --version
You should see the installed Python version (e.g., Python 3.11.5).
```

### Install pip:

Pip is usually installed automatically with Python. Verify it by running:
```
pip --version
```

2. Open Folder

- Navigate to the **Employee Management** folder 

3. Install Requirements

You can install all the required dependencies using the requirements.txt file. Run the following command:
```
pip install -r requirements.txt
```

4. Run the Application

Run the command
```
python app.py
```

5. Access the Application

Open your browser and navigate to:

http://127.0.0.1:5000/


## Project Structure

employee-management-system/
│
├── app.py                     # Main Flask application file
├── requirements.txt           # List of Python dependencies
│
├── static/
│   └── styles.css             # CSS file for styling the frontend
│
└── templates/
    ├── index.html             # Homepage to display and add employees
    └── edit.html              # Page to edit employee details


## Usage


***Homepage:***

View the list of employees.

Add a new employee using the form at the bottom of the page.

***Edit Employee:***

Click the "Edit" button next to an employee to update their details.

***Delete Employee:***

Click the "Delete" button next to an employee to remove them from the database (with a confirmation prompt).

