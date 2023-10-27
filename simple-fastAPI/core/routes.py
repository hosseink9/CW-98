from fastapi.routing import APIRouter
from fastapi import status, HTTPException
from .schemas import BookRequest
from .db import core_collection
from bson.objectid import ObjectId
from typing import List
from fastapi import Depends
from authentication.deps import get_current_user

router = APIRouter(tags=["core"])

@router.get("/", status_code=status.HTTP_200_OK)
async def retrieve_books():
    books = []
    for book in core_collection.find():
        book["_id"] = str(book["_id"])
        books.append(book)
    return books


@router.post("/add_book", status_code=status.HTTP_201_CREATED)
async def add_book(book: BookRequest, user=Depends(get_current_user)):
    print(user)
    result = core_collection.insert_one(dict(book))
    ack = result.acknowledged
    return {"insertion": ack}


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_book(book_id):
    result = core_collection.find_one_and_delete({"_id":ObjectId(book_id)})
    if result == False:
        raise Exception
    return {"message":"book was deleted"}



# @router.get('/')
# def get_notes():
#     return "return a list of note items"


# @router.post('/', status_code=status.HTTP_201_CREATED)
# def create_note():
#     return "create note item"


# @router.patch('/{noteId}')
# def update_note(noteId: str):
#     return f"update note item with id {noteId}"


# @router.get('/{noteId}')
# def get_note(noteId: str):
#     return f"get note item with id {noteId}"



