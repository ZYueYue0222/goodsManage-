from fastapi import FastAPI
from app.router import goods
from fastapi.middleware.cors import CORSMiddleware
from app.get_db import create_tables

app=FastAPI(title="商品管理系统API")

create_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(goods.router)
