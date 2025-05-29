# seeders/main.py
from sqlalchemy.orm import Session

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.config.database import engine
from seeders.users import seed_users

def run_all_seeders(db: Session):
    print("🚀 Running seeders...")
    seed_users(db)
    print("🎉 Seeding complete.")

def main():
    with Session(engine) as session:
        run_all_seeders(session)

if __name__ == "__main__":
    main()
