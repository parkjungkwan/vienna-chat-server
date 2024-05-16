from fastapi import APIRouter
from pydantic import BaseModel
from icecream import ic
from app.api.titanic.service.titanic_service import TitanicService
CONTEXT = 'C:\\Users\\bitcamp\\kubernetes\\chat-server\\backend\\app\\api\\context\\'


router = APIRouter()
service = TitanicService()

class Request(BaseModel):
    question: str

class Response(BaseModel):
    answer: str

@router.post("/titanic")
async def titanic(req:Request):
    ic('타이타닉 딕셔너리 내용')
    hello = f'{CONTEXT}data\\hello.txt'
    f = open(hello, "r", encoding="utf-8")
    data = f.read()
    ic(data)
    f.close()
    service.preprocess()
    ic(req)
    return {"answer": "생존자는 100명이야."}

