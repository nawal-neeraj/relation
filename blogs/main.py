from fastapi import FastAPI
from .schema import schema
from .Database.database import engine
from .controller import (
    blogs,
    users,
    profiles
)
 
schema.Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(profiles.router)
