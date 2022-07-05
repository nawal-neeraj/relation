from fastapi import FastAPI
from .schema import schema
from .Database.database import engine
from .data_store import (
    blogs, 
    register, 
    users, 
    profiles,
)
 
schema.Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(blogs.router)
app.include_router(register.router)
app.include_router(users.router)
app.include_router(profiles.router)
