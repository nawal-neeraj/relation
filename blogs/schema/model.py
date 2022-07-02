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
    
    
class UserProfile(BaseModel):
    id: Optional[int]= None
    phone: str
    email: str
    user_id: int
    
class ShowProfile(BaseModel):
    id: Optional[int]= None
    phone: str
    email: str
    user_id: int
    
class ProfileResponse(BaseModel):
    phone: str
    email: str
    user_id: int
    class Config():
        orm_mode = True
    
class ProfileRes(BaseModel):
    email: str
    class Config():
        orm_mode = True
        
class ShowProfile(BaseModel):
    id: int
    phone: str
    details: ProfileRes
    class Config():
        orm_mode = True