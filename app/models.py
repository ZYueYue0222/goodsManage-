from sqlalchemy import Column,INTEGER,String
from app.get_db import Base

class Goods(Base):
    __tablename__="goods"
    id=Column(INTEGER,primary_key=True,autoincrement=True)
    bh=Column(String(50),nullable=False)
    name=Column(String(50),nullable=False)
    types=Column(String(50),nullable=False)
    price=Column(String(50),nullable=False)
    stock = Column(INTEGER, nullable=False, default=0)