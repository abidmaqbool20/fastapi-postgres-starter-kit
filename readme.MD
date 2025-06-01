# 🚀 FastAPI Project

A modern Python web API built with [FastAPI](https://fastapi.tiangolo.com/), SQLAlchemy, Alembic, and PostgreSQL.

---

## 📦 Features

- FastAPI for high-performance APIs
- SQLAlchemy for ORM
- Alembic for migrations
- Seeders for populating initial data
- PostgreSQL (or SQLite) as the database
- Modular structure for scalability

---

## 🛠️ Setup Instructions

### 1. 📥 Clone the repository

```bash
git clone https://github.com/your-username/fastapi-project.git
cd fastapi-project

### 2. 📥 Install the dependencies

```bash
pip install -r requirements.txt

### 3. 📥 Run migrations

```bash
alembic revision --autogenerate -m "add your message here" ### To generate migrations from the model
alembic upgrade head ### To run migrations


### 4. 📥 Run seeder

```bash
python seeders/main.py

### 4. 📥 Execute project

```bash
uvicorn main:app --reload
