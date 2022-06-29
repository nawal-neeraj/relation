from typing import List, Optional
from pydantic import BaseModel

class Blogs(BaseModel):
    id: Optional[int]= None
    title: str
    body: str

class Show_user(BaseModel):
    name: str
    email: str
    blog: List
    class Config():
        orm_mode = True

class Users(BaseModel):
    id: Optional[int]= None
    name: str
    email: str
    password: str
    
class user_resp(BaseModel):
    id: int
    name: str
    email: str
    class Config():
        orm_mode = True
    
    
class Show_blogs(BaseModel):
    id: int
    title:str
    body:str
    creator: user_resp
    
    class Config():
        orm_mode = True