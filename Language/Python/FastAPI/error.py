import uvicorn  # 실행모듈

from fastapi import FastAPI, Query, Path, Body, Form  # API관련 모듈
from fastapi import File, UploadFile
from fastapi import HTTPException


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not fount",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}


if __name__ == "__main__":
    uvicorn.run("error:app", port=8000, reload=True)
