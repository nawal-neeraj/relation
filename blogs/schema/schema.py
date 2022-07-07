from sqlalchemy import Column, Integer, String, ForeignKey
from ..Database.database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'
    blog_id: int = Column('id',Integer, primary_key=True, index=True)
    title = Column(String(20), index=True)
    body = Column(String(20), index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates="blog")


class User(Base):
    __tablename__ = 'users'

    user_id: int = Column('id',Integer, primary_key=True, index=True)
    name = Column(String(20), index=True)
    email = Column(String(20), index=True)
    password = Column(String(2000), index=True)

    blog = relationship("Blog", back_populates="creator")
    profile = relationship("Profile", back_populates="details")


class Profile(Base):
    __tablename__ = 'profile'

    profile_id: int = Column('id',Integer, primary_key=True, index=True)
    phone = Column(String(255), index=True)
    email = Column(String(255), index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    details= relationship("User", back_populates="profile")
    