# seeders/main.py
from sqlalchemy.orm import Session

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.config.database import engine
from seeders.users import seed_users
from seeders.roles import seed_roles
from seeders.user_role_seeder import seed_user_roles

def run_all_seeders(db: Session):
    try:
        print("🚀 Running seeders...")
        seed_users(db)
        seed_roles(db)
        seed_user_roles(db)
        print("🎉 Seeding complete.")
    finally:
        db.close()
def main():
    with Session(engine) as session:
        run_all_seeders(session)

if __name__ == "__main__":
    main()
