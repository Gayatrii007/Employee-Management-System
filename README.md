# Employee Management System (Django REST API)

This project is a backend **Employee Management System** built using **Django REST Framework** as part of an assignment.  
It provides secure authentication and RESTful APIs to manage employees.

---

## Assignment Highlights

- Secure JWT authentication
- Login using **username OR email**
- RESTful API design
- Proper validations and error handling
- Soft delete implementation
- Clean and scalable code structure

---

## Tech Stack

| Technology | Purpose |
|----------|--------|
| Python | Programming language |
| Django | Backend framework |
| Django REST Framework | API development |
| Simple JWT | Authentication |
| SQLite | Local database |

---

## Project Structure

employee_management/
│
├── employee_management/
│ ├── settings.py
│ ├── urls.py
│
├── employees/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ ├── backends.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
├── README.md

yaml
Copy code

---

## Authentication

JWT authentication is used.  
After login, include the token in headers:

Authorization: Bearer <access_token>

pgsql
Copy code

### Login API

**POST** `/api/login/`

#### Login using Username
```json
{
  "username": "admin",
  "password": "your_password"
}
Login using Email
json
Copy code
{
  "email": "admin@gmail.com",
  "password": "your_password"
}
Successful Response
json
Copy code
{
  "refresh": "jwt_refresh_token",
  "access": "jwt_access_token"
}
Employee APIs
Method	Endpoint	Description
GET	/api/employees/	Get all employees
POST	/api/employees/	Create new employee
GET	/api/employees/{id}/	Get employee by ID
PUT	/api/employees/{id}/	Update employee
DELETE	/api/employees/{id}/	Soft delete employee

🔒 All endpoints require JWT authentication

Database Design
Employee Table
Column Name	Type	Description
id	Integer	Primary key
name	String	Employee full name
email	String	Unique employee email
department	String	Employee department
designation	String	Employee role
date_of_joining	Date	Joining date
status	String	Active / Inactive
created_at	DateTime	Record creation time
updated_at	DateTime	Record last update time

Business Rules & Validations
Email must be unique

Password is mandatory for login

Either username or email is required for authentication

Employee with future joining date cannot be Active

Soft delete is implemented using status field

How Database Tables Are Created
Models are defined in models.py

Create migration files:

bash
Copy code
python manage.py makemigrations
Apply migrations:

bash
Copy code
python manage.py migrate
Django ORM automatically manages schema creation.

How to Run the Project
bash
Copy code
git clone https://github.com/Gayatrii007/Employee-Management-System.git
cd Employee-Management-System
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Server will run at:

cpp
Copy code
http://127.0.0.1:8000/
Author
Gayatri Babhulkar
B.Tech – Computer Science Engineering
Backend Developer (Python / Django)