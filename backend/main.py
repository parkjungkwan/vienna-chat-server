from fastapi import FastAPI
from langchain.chat_models.openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv
import uvicorn
from app.main_router import router
from icecream import ic

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

from pydantic import BaseModel

from starlette.middleware.cors import CORSMiddleware


class Request(BaseModel):
    question: str

class Response(BaseModel):
    answer: str


app = FastAPI()

app.include_router(router, prefix="/api")

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.post("/chat")
def chatting(req:Request):
    ic(req)
    # template = PromptTemplate.from_template("{country}의 수도는 어디야 ?")
    # template.format(country=req.question)
 
    chat = ChatOpenAI(
        openai_api_key=os.environ["api_key"],
        temperature=0.1,               # 창의성 (0.0 ~ 2.0) 
        max_tokens=2048,             # 최대 토큰수
        model_name='gpt-3.5-turbo-0613',  # 모델명
        )


    # 질의
    ic(f'{chat.predict(req.question)}')
    


    # message = [
    #     SystemMessage(content="You are a traveler. I know the capitals of every country in the world.", type="system"),
    #     HumanMessage(content="{country}의 수도는 어디야 ? ", type="human"),
    #     AIMessage(content="서울 입니다.", type="ai"),
    # ]


    return Response(answer=chat.predict(req.question))

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    import os
    import uvicorn
    os.chdir(os.getcwd() )
    ic(f'{os.getcwd()}')
    uvicorn.run(app, host="localhost", port=8000)
