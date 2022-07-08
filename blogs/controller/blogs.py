from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session

from ..Database.database import get_db

from ..schema.model import (
    ShowBlogs,
    Blogs,
    )
from ..schema import schema

router = APIRouter(
    prefix="/blog",
    tags=['blog']
)

@router.get('/{id}', tags=['blog'], response_model=ShowBlogs)
def get_blog(id: int, db: Session = Depends(get_db)):
    new_blog = db.query(schema.Blog).filter(schema.Blog.user_id == id).first()
    return new_blog


@router.post('/blog')
def add_blog(request: Blogs, db: Session = Depends(get_db)):
    new_blog = schema.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

