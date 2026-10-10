from sys import exception
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.get_db import get_db
from app.models import Goods
from app.pydantic_model import GoodsCreate,GoodsRead,GoodsUpdate
from app.pagination import pagination

router=APIRouter()

# 渲染
@router.get("/list")
def getlist(
    keyword:Optional[str]=None,
    db:Session=Depends(get_db),
    pages=Depends(pagination)
):
    res=db.query(Goods)
    if keyword:
        res=res.filter(or_(Goods.name.like(f"%{keyword}%"),Goods.types.like(f"%{keyword}%")))
    total=res.count()
    data=res.offset(pages["skip"]).limit(pages["pageSize"]).all()
    return {"total":total,"data":data}

# 新增
@router.post("/add",status_code=status.HTTP_201_CREATED)
def add_goods(form:GoodsCreate,db:Session=Depends(get_db)):
    res=Goods(**form.model_dump())
    db.add(res)
    db.commit()
    db.refresh(res)
    return {"msg":"新增成功","data":res}
# 修改
@router.put("/edit/{id}")
def edit_goods(id:int,form:GoodsUpdate,db:Session=Depends(get_db)):
    res=db.query(Goods).get(id)
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="未找到该商品")
    info=form.model_dump(exclude_unset=True)
    for k,v in info.items():
        setattr(res,k,v)
    db.commit()
    db.refresh(res)
    return {"msg":"修改成功","data":res}
# 删除
@router.delete("/delete_goods/{id}")
def delete_goods(id:int,db:Session=Depends(get_db)):
    res=db.query(Goods).get(id)
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="未找到该商品")
    db.delete(res)
    db.commit()
    return {"msg":"删除成功"}
# 详情
@router.get("/get_one/{id}",response_model=GoodsRead)
def get_one(id:int,db:Session=Depends(get_db)):
    res=db.query(Goods).get(id)
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="未找到该商品")
    return res