from pydantic import BaseModel
from typing import List, Optional, Union
from fastapi import Query, Path

class BookResponse(BaseModel):
    _id: str
    title: str
    author:str
    publisher: str


class BookRequest(BaseModel):
    title: str
    author:str
    publisher: str
