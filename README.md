# Employee Management System (Django REST API)

A backend Employee Management System built using **Django REST Framework** as part of an assignment.

This project provides secure authentication and RESTful APIs to manage employees with proper validations and clean architecture.

---

## ✅ Assignment Highlights

- Secure JWT authentication
- Login using **username OR email**
- RESTful API design
- Proper validations and error handling
- Soft delete implementation
- Clean and scalable code structure

---

## 🔐 Authentication

JWT (JSON Web Token) authentication is used.

All protected APIs require the following header:

```
Authorization: Bearer <access_token>
```

---

## 🔑 Login API

### POST `/api/login/`

### Login using Username
```json
{
  "username": "admin",
  "password": "your_password"
}
```

### Login using Email
```json
{
  "email": "admin@gmail.com",
  "password": "your_password"
}
```

### Successful Response
```json
{
  "refresh": "jwt_refresh_token",
  "access": "jwt_access_token"
}
```

---

## 👩‍💼 Employee APIs

### Employee Endpoints

| Method | Endpoint                  | Description               |
|------|---------------------------|---------------------------|
| GET  | `/api/employees/`         | Get all employees         |
| POST | `/api/employees/`         | Create a new employee     |
| GET  | `/api/employees/{id}/`    | Get employee by ID        |
| PUT  | `/api/employees/{id}/`    | Update employee           |
| DELETE | `/api/employees/{id}/`  | Soft delete employee      |

🔒 **All endpoints require JWT authentication**

---

## 🗄 Database Design

### Employee Table

| Column Name     | Type     | Description                    |
|-----------------|----------|--------------------------------|
| id              | Integer  | Primary key                    |
| name            | String   | Employee full name             |
| email           | String   | Unique employee email          |
| department      | String   | Employee department            |
| designation     | String   | Employee role                  |
| date_of_joining | Date     | Joining date                   |
| status          | String   | Active / Inactive              |
| created_at      | DateTime | Record creation time           |
| updated_at      | DateTime | Record last update time        |

---

## 📏 Business Rules & Validations

- Email must be **unique**
- Password is **mandatory** for login
- Either **username or email** is required for authentication
- Employee with a **future joining date cannot be Active**
- Soft delete marks employee as inactive instead of removing data

---

## 🧠 How Database Tables Are Created

1. Models are defined in `employees/models.py`
2. Create migration files:
   ```bash
   python manage.py makemigrations
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

Django ORM automatically manages schema creation.

---

## ⚙ Tech Stack

| Technology | Purpose |
|----------|---------|
| Python | Programming language |
| Django | Backend framework |
| Django REST Framework | API development |
| Simple JWT | Authentication |
| SQLite | Database (local development) |

---

## 📂 Project Structure

```
employee_management/
│
├── employee_management/
│   ├── settings.py
│   ├── urls.py
│
├── employees/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── backends.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
├── README.md
```

---

## ▶ How to Run the Project

```bash
git clone https://github.com/Gayatrii007/Employee-Management-System.git
cd Employee-Management-System
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000/
```

---

## 👩‍💻 Author

**Gayatri Babhulkar**  
gayatrin3babhulkar@gmail.com
