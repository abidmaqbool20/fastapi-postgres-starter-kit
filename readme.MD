# 🚀 FastAPI Project Starter Kit

A modern, scalable API boilerplate built with **FastAPI**, **SQLAlchemy**, **JWT-based Authentication**, **Alembic**, and **PostgreSQL**. This project provides everything you need to kickstart your backend with clean architecture and essential features out of the box.

---

## 📦 Features

* ⚡️ FastAPI for high-performance APIs
* 💃 SQLAlchemy for ORM and models
* 🔐 JWT-based Authentication
* 👥 Role-based Authorization
* 🔄 Alembic for seamless migrations
* 🌱 Seeders to populate initial data
* 🐘 PostgreSQL or SQLite as database
* 📂 Modular and scalable project structure
* 🧹 Centralized constants and config
* ✅ Migrations fully integrated

---

## 🚀 Getting Started — Step by Step

### Step 1: 📥 Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-project.git
cd fastapi-project
```

---

### Step 2: 📦 Set Up a Virtual Environment and Install Dependencies

#### For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### For Windows:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

### Step 3: ⚙️ Create a `.env` Configuration File

Create a `.env` file in the root directory and add your environment-specific variables:

```ini
DATABASE_URL=postgresql://username:password@localhost:5432/db_name
SECRET_KEY=your_jwt_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> 💡 You can also use SQLite for local testing:
>
> ```ini
> DATABASE_URL=sqlite:///./test.db
> ```

---

### Step 4: 🔄 Run Database Migrations

#### Create a new migration:

```bash
alembic revision --autogenerate -m "Initial migration"
```

#### Apply migrations:

```bash
alembic upgrade head
```

---

### Step 5: 🌱 Seed Initial Data

Populate the database with initial roles, users, or other constants:

```bash
python seeders/main.py
```

---

### Step 6: 🚀 Run the FastAPI Server

Start the development server with hot-reload:

```bash
uvicorn main:app --reload
```

> Open your browser and go to:
>
> * Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
> * ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📁 Project Structure

```
.
├── alembic/                # Alembic migration scripts
├── app/
│   ├── core/               # Configuration, constants, security
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic schemas (request/response)
│   ├── routers/            # API endpoints
│   ├── services/           # Business logic
│   └── main.py             # FastAPI entry point
├── seeders/                # Database seed scripts
├── alembic.ini             # Alembic configuration
├── requirements.txt        # Project dependencies
└── .env.example            # Sample environment config
```

---

## ✅ Roadmap

* [x] FastAPI setup
* [x] JWT authentication
* [x] Role-based access control
* [x] Alembic migrations
* [x] Seeder implementation
* [ ] Docker + Docker Compose support
* [ ] Unit and integration tests
* [ ] GitHub Actions CI/CD

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit a pull request to improve the project.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ✨ Credits

Made with ❤️ using [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/), and [PostgreSQL](https://www.postgresql.org/).
