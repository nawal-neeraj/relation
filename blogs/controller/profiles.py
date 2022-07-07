from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session

from ..Database.database import SessionLocal, engine, get_db
from ..hasher.hash import verify_passwor
from ..schema.model import (
    ProfileResponse,
    UserProfile,
    ShowProfile
    )
from ..schema import schema
from ..datalayer.register import register_user_profile

router = APIRouter(
    prefix="/profile",
    tags=['profiles']
)


@router.post('/', response_model=ProfileResponse)
def add_profile(request: UserProfile, db: Session = Depends(get_db)):
    new_user = register_user_profile(request, db)
    return new_user

@router.get('/show_profile/user_id:{id}', response_model=ShowProfile)
def show_profile(id: int, db: Session = Depends(get_db)):
    new_user = db.query(schema.Profile).filter(schema.Profile.profile_id == id).first()
    return new_user