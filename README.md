# codsoft Task 1: To-Do List Application

A feature-rich, responsive, full-stack **To-Do List Application** built with **Python**, **Django**, **MySQL**, and **Bootstrap 5** for the **CodSoft Internship Program**.

---

## 🌟 Features

- **Full Task Lifecycle Management (CRUD)**: Create, View, Edit, and Delete tasks easily.
- **Quick Status Toggle**: Mark tasks as completed or reopen them with one click.
- **Priority & Categorization**: Organize tasks by Category (`Work`, `Personal`, `Study`, `Other`) and Priority (`High`, `Medium`, `Low`).
- **Interactive Search & Filtering**: Instant search across titles & descriptions, plus filtering by status, priority, or category.
- **Real-Time Task Dashboard**: Live counters for Total Tasks, Pending, In Progress, and Completed tasks.
- **Dual Database Support**: Direct integration with **MySQL**, with automatic fallback to **SQLite3** if MySQL credentials are not configured.
- **Responsive UI**: Modern interface with high-contrast badge colors and FontAwesome icons.

---

## 📁 Project Architecture

```
codsoft_taskno1_to-do-list/
│
├── manage.py                # Django administrative entry point
├── setup_db.py              # MySQL database auto-creation and setup script
├── seed_demo_data.py        # Seed script for initial sample data
├── .env                     # Local environment settings (MySQL DB credentials)
├── .env.example             # Configuration template
│
├── todo_project/            # Django project settings & configuration
│   ├── settings.py          # MySQL / SQLite DB backend & app setup
│   ├── urls.py              # Root URL router
│   └── wsgi.py              # WSGI server entrypoint
│
└── tasks/                   # Tasks application logic
    ├── models.py            # Task data model definition
    ├── views.py             # CRUD & search/filtering view functions
    ├── forms.py             # Bootstrap-styled model forms
    ├── urls.py              # Application route definitions
    ├── tests.py             # Automated unit tests
    └── templates/tasks/     # HTML5 templates (base, task_list, task_form, task_confirm_delete)
```

---

## 🚀 How to Run the Application

### 1. Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate
```

### 2. Configure MySQL Credentials (Optional)
Edit the `.env` file in the project root folder to set your MySQL server password:

```ini
USE_MYSQL=true
DB_NAME=todo_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

> **Note**: If `USE_MYSQL=false` or if MySQL server connection fails, the application automatically uses SQLite3 (`db.sqlite3`).

### 3. Initialize Database & Apply Migrations
```bash
# Verify database connection and create DB if using MySQL
python setup_db.py

# Apply migrations
python manage.py migrate

# Seed sample data for testing (Optional)
python seed_demo_data.py
```

### 4. Run the Development Server
```bash
python manage.py runserver
```

Open your web browser and navigate to: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🧪 Running Automated Tests

To run the unit test suite:

```bash
python manage.py test tasks
```

---

## 📜 License & Acknowledgments
Created as part of the **CodSoft Python Development Internship Task 1**.
