from typing import List, Optional
from pydantic import BaseModel

class Blogs(BaseModel):
    id: Optional[int]= None
    title: str
    body: str

class ShowUser(BaseModel):
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
    
class UserResp(BaseModel):
    id: int
    name: str
    email: str
    class Config():
        orm_mode = True
    
    
class ShowBlogs(BaseModel):
    id: int
    title:str
    body:str
    creator: UserResp
    
    class Config():
        orm_mode = True
        

class Login(BaseModel):
    id: int
    password: str