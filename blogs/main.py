from fastapi import FastAPI, Depends
from .schema.model import (
    Blogs, 
    Users, 
    UserResp, 
    ShowBlogs, 
    ShowUser,
    Login
    )
from .schema import schema
from sqlalchemy.orm import Session
from .Database.database import SessionLocal, engine, get_db
from .hasher.hash import hash_passwor, verify_passwor
 
schema.Base.metadata.create_all(engine)
app = FastAPI()


@app.post('/blog', tags=['blog'])
def create(request: Blogs, db: Session = Depends(get_db)):
    new_blog = schema.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.post('/blog/{id}', tags=['blog'], response_model=ShowBlogs)
def create(id: int, db: Session = Depends(get_db)):
    new_blog = db.query(schema.Blog).filter(schema.Blog.id == id).first()
    return new_blog


@app.post('/user', response_model=UserResp, tags=['user'])
def create(request: Users, db: Session = Depends(get_db)):
    new_user = schema.User(name=request.name, email=request.email, password=hash_passwor(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post('/show_user/{id}', tags=['user'], response_model=ShowUser)
def create(id: int, db: Session = Depends(get_db)):
    new_user = db.query(schema.User).filter(schema.User.id == id).first()
    return new_user

@app.post('/log_user', tags=['user'])
def create(request: Login, db: Session = Depends(get_db)):
    print(request.id)
    new_user = db.query(schema.User).filter(schema.User.id == request.id).first()
    print(new_user.id)
    check_password = verify_passwor(request.password, new_user.password)
    print(check_password)
    return new_user