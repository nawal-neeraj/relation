from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session

from ..Database.database import SessionLocal, engine, get_db

from ..schema.model import (
    Blogs,
    Users,
    UserResp 
    )
from ..schema import schema
from ..hasher.hash import hash_passwor


router = APIRouter(
    prefix="/register",
    tags=['register']
)

get_db = get_db

@router.post('/blog')
def add_blog(request: Blogs, db: Session = Depends(get_db)):
    new_blog = schema.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.post('/user', response_model=UserResp)
def add_user(request: Users, db: Session = Depends(get_db)):
    new_user = schema.User(name=request.name, email=request.email, password=hash_passwor(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user