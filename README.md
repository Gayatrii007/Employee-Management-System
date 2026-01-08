POST /api/login/


### Login using Username
```json
{
  "username": "admin",
  "password": "your_password"
}

Login using Email
{
  "email": "admin@gmail.com",
  "password": "your_password"
}

Successful Response
{
  "refresh": "jwt_refresh_token",
  "access": "jwt_access_token"
}


🔒 Use the access token in headers:

Authorization: Bearer <access_token>

## 👨‍💻 Employee APIs

### Employee Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/employees/` | Get all employees |
| POST | `/api/employees/` | Create a new employee |
| GET | `/api/employees/{id}/` | Get employee by ID |
| PUT | `/api/employees/{id}/` | Update employee |
| DELETE | `/api/employees/{id}/` | Soft delete employee |

🔐 **All endpoints require JWT authentication**

## 🗄 Database Design

### Employee Table

| Column Name | Type | Description |
|-------------|------|-------------|
| id | Integer | Primary Key |
| name | String | Employee full name |
| email | String | Unique employee email |
| department | String | Employee department |
| designation | String | Employee role |
| date_of_joining | Date | Joining date |
| status | String | Active / Inactive |
| created_at | DateTime | Record creation time |
| updated_at | DateTime | Record last update time |

📜 Business Rules & Validations

Email must be unique

Password is mandatory for login

Either username OR email must be provided for authentication

Employee with a future joining date cannot be Active

Delete operation performs soft delete (status → INACTIVE)

⚙️ Project Setup (Local)
1️⃣ Clone Repository
git clone https://github.com/Gayatrii007/Employee-Management-System.git
cd Employee-Management-System

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Database Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Admin User
python manage.py createsuperuser

6️⃣ Run Development Server
python manage.py runserver


Server will run at:

http://127.0.0.1:8000/

🧠 How Database Tables Are Created

Models are defined in models.py

Migration files are generated using:

python manage.py makemigrations


Tables are created in the database using:

python manage.py migrate


Django ORM automatically manages schema creation and updates.

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python | Programming language |
| Django | Backend framework |
| Django REST Framework | API development |
| Simple JWT | Authentication |
| SQLite | Database (local development) |

📁 Project Structure
employee_management/
├── employees/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── backends.py
│   └── urls.py
├── employee_management/
│   ├── settings.py
│   ├── urls.py
├── manage.py
├── requirements.txt
└── README.md

✅ Assignment Highlights

Secure JWT authentication

Username or email based login

RESTful API design

Proper validations and error handling

Soft delete implementation

Clean and scalable code structure

👩‍💻 Author

Gayatri Babhulkar
B.Tech – Computer Science Engineering
Backend Developer (Python / Django)