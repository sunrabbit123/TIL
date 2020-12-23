import uvicorn #실행모듈

from fastapi import FastAPI, Query, Path, Body, Form#API관련 모듈
from fastapi import File, UploadFile
from fastapi import HTTPException

from typing import Optional, List, Set, Dict, Union#잡 모듈
from pydantic import BaseModel, HttpUrl, EmailStr



app = FastAPI()

class Image(BaseModel):
    url : HttpUrl
    name : str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    List_tags: List[str] = []
    Set_tags: Set[str] = set()
    image: Optional[List[Image]] = None
items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

class Offer(BaseModel):
    name : str
    description: Optional[str] = None
    price: float
    items: List[Item]

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class UserIn(UserBase):
    password : str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str

class BaseItem(BaseModel):
    description: str
    type: str

class CarItem(BaseItem):
    type = 'car'
    type = 'plane'

class PlaneItem(BaseItem):
    type = "plane"
    size : int


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db

@app.post("/user/", response_model=UserOut)
async def craete_user(user : UserIn):
    user_saved = fake_save_user(user)
    return user_saved


@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.post("/items/", response_model=Item, response_model_exclude_unset=True, status_code=201
                                        # response_model_exclude_defaults=True
                                        # response_model_exclude_none=True
            response_description="The created item")
async def create_item(item: Item):
    return item

@app.get('/items/{item_id}',
        response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404,
                            detail="Item not fount",
                            headers = {"X-Error" : "There goes my error"})
    return items[item_id]
    

@app.post("/item/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded
    

@app.post("/offers/")
async def create_offer(offer : Offer):
    return offer

@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images

@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights

@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo" : 2.3, "bar" : 3.4}

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username" : username}

@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}

@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}


# @app.put("/items/{item_id}")
# async def update_item(
#     *, 
#     item_id: int,
#     item: Item = Body(..., embed=True),
#     user: User,
#     importance: int,
#     q: Optional[str] = None
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     if q:
#         results.update({"q": q})
#     return results


if __name__ == "__main__":
    uvicorn.run("main:app", port = 8000, reload = True)
