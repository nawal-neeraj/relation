from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session

from ..Database.database import SessionLocal, engine, get_db
from ..hasher.hash import verify_passwor
from ..schema.model import (
    ShowUser,
    Login,
    UserResp,
    Users
    )
from ..schema import schema
from ..datalayer.register import register_user

router = APIRouter(
    prefix="/users",
    tags=['users']
)

@router.get('/show_user/{id}', response_model=ShowUser)
def show_user(id: int, db: Session = Depends(get_db)):
    new_user = db.query(schema.User).filter(schema.User.user_id == id).first()
    return new_user


@router.post('/login_user')
def user_login(request: Login, db: Session = Depends(get_db)):
    new_user = db.query(schema.User).filter(schema.User.id == request.id).first()
    check_password = verify_passwor(request.password, new_user.password)
    if not check_password:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED)
    return new_user

@router.post('/add_user', response_model=UserResp)
def add_user(request: Users, db: Session = Depends(get_db)):
    new_user =register_user(request, db)
    return new_user