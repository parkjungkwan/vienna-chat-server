from fastapi import FastAPI
import uvicorn

from example.bmi import BMI
from example.rps import RPS

app = FastAPI()


@app.get("/")
async def root():
    this = RPS()
    this.play()
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)