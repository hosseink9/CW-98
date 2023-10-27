from pydantic import BaseModel
from typing import List, Optional, Union
from fastapi import Query, Path

class UserIn(BaseModel):
    username: str | None=None
    password: str | None=None
    firstname: str | None=None
    lastname: str | None=None

class UserOut(BaseModel):
    _id: str
    username: str
    firstname: str | None=None
    lastname: str | None=None
    class config:
        orm_mode = True

class UserUpdate(BaseModel):
    username: str | None=None
    firstname: str | None=None
    lastname: str | None=None

class TokenPayload(BaseModel):
    access_token: str = 'access_token'
    refresh_token: str = 'refresh_token'
    exp: str = 'exp'
