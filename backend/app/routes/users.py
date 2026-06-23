from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import User
from ..schemas import UserCreate, UserLogin
from ..security import hash_password, verify_password
from ..auth import create_access_token
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        return {"message": "Email already registered"}

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.user_id
    }


@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        return {"message": "Invalid email"}

    if not verify_password(
        user.password,
        db_user.password
    ):
        return {"message": "Invalid password"}

    token = create_access_token(
    {
        "user_id": db_user.user_id,
        "email": db_user.email
    }
)

    return {
    "message": "Login successful",
    "user_id": db_user.user_id,
    "access_token": token,
    "token_type": "bearer"
}