import uvicorn
from fastapi import FastAPI
from markupsafe import escape
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"Hello": "World"}


@app.get("/hello/{name}")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.get("/gugudan/")
def gugudan(dan: int = 2):
    return f"구구단 {dan}단 출력"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
