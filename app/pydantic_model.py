from pydantic import BaseModel


class GoodsCreate(BaseModel):
    bh:str
    name:str
    types:str
    price:str
    stock:int

class GoodsUpdate(BaseModel):
    bh:str|None=None
    name:str|None=None
    types:str|None=None
    price:str|None=None
    stock:int|None=None

class GoodsRead(BaseModel):
    id:int
    bh:str
    name:str
    types:str
    price:str
    stock:int
    model_config={"from_attributes":True}