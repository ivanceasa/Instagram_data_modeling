import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    # Here we define columns for the table 
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    lastname = Column(String(50))
    username = Column(String(50))
    email = Column(String(50), nullable=False)


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    post_content = Column(String(250), nullable=False)
    date = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    date = Column(String(50), nullable=False)
    author_id = Column(Integer, ForeignKey("user.id")) 
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
        

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e