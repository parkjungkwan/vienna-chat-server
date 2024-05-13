from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Request(BaseModel):
    question: str

class Response(BaseModel):
    answer: str

@router.post("/titanic")
async def titanic(req:Request):
    print('타이타닉 딕셔너리 내용')
    hello = 'C:\\Users\\bitcamp\\kubernetes\\chat-server\\backend\\app\\api\\titanic\\data\\hello.txt'
    f = open(hello, "r", encoding="utf-8")
    data = f.read()
    print(data)
    f.close()

    print(req)
    return {"answer": "생존자는 100명이야."}

