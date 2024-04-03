from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from datetime import datetime #small letter only

base = declarative_base()

class User(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    email = Column(String(50), unique=True)
    password = Column(String(64))
    created_at = Column(DateTime, default=datetime.now)

class Message(base):
    __tablename__ ="messages"
    id = Column(Integer,primary_key=True)
    message= Column(String(255))
    user_id = Column(Integer,ForeignKey("users.id"))
    Created_at =Column(DateTime,default=datetime.now)


#
if __name__ == "__main__":
    engine = create_engine("sqlite:///example.db")
    base.metadata.create_all(engine)
