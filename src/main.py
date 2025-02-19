import uvicorn
from fastapi import FastAPI
from web import square

app = FastAPI()

app.include_router(square.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)