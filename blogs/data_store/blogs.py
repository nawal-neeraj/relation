from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session

from ..Database.database import SessionLocal, engine, get_db

from ..schema.model import (
    ShowBlogs, 
    )
from ..schema import schema

router = APIRouter(
    prefix="/blog",
    tags=['blog']
)

get_db = get_db

@router.get('/{id}', tags=['blog'], response_model=ShowBlogs)
def get_blog(id: int, db: Session = Depends(get_db)):
    new_blog = db.query(schema.Blog).filter(schema.Blog.user_id == id).first()
    return new_blog