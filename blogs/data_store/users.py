from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session

from ..Database.database import SessionLocal, engine, get_db
from ..hasher.hash import verify_passwor
from ..schema.model import (
    ShowUser,
    Login
    )
from ..schema import schema

router = APIRouter(
    prefix="/users",
    tags=['users']
)

get_db = get_db

@router.get('/show_user/{id}', response_model=ShowUser)
def show_user(id: int, db: Session = Depends(get_db)):
    new_user = db.query(schema.User).filter(schema.User.user_id == id).first()
    return new_user


@router.post('/log_user')
def user_login(request: Login, db: Session = Depends(get_db)):
    new_user = db.query(schema.User).filter(schema.User.id == request.id).first()
    check_password = verify_passwor(request.password, new_user.password)
    if not check_password:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED)
    return new_user