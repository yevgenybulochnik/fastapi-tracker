import uvicorn
from fastapi import FastAPI

from trackerapi import models
from trackerapi.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World bla"}


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, debug=True)
