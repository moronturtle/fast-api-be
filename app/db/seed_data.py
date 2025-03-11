import os
import uuid
from dotenv import load_dotenv  # Add this
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models.user import User, UserRole

# Load .env file
load_dotenv()

def seed_admin():
    db: Session = SessionLocal()

    admin_exists = db.query(User).filter(User.role == UserRole.superadmin).first()

    if not admin_exists:
        print("Seeding superadmin user...")
        superadmin = User(
            id=uuid.uuid4(),
            name=os.getenv("SUPERADMIN_NAME", "defaultadmin"),
            email=os.getenv("SUPERADMIN_EMAIL", "admin@example.com"),
            role=UserRole.superadmin,
        )
        db.add(superadmin)
        db.commit()
        print("Superadmin created successfully.")
    else:
        print("Superadmin already exists, skipping seeding.")

    db.close()

if __name__ == "__main__":
    RUN_SEED = os.getenv("RUN_SEED", "False").lower() == "true"
    print(f"RUN_SEED: {RUN_SEED}")
    if RUN_SEED:
        seed_admin()
    else:
        print("Seeding skipped, RUN_SEED is not set to 'true'.")
