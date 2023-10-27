from bson import ObjectId
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.routing import APIRouter
from fastapi.responses import RedirectResponse
from .schemas import UserOut, UserIn, UserUpdate
from .deps import get_current_user
from core.db import users_collection
# from core import db
from .utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)
from uuid import uuid4

routes = APIRouter(tags=["authentication"])

@routes.post('/signup', summary="Create new user", response_model=UserOut)
async def create_user(data: UserIn):
    # querying database to check if user already exist
    user = users_collection.find_one({'username':data.username})
    if user is not None:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="User with this username already exist"
        )
    user = {
        'username': data.username,
        'password': get_hashed_password(data.password),
        'id': str(uuid4())
    }
    users_collection.insert_one(dict(user))   # saving user to database
    return user


@routes.post('/login', summary="Create access and refresh tokens for user")
async def login(data: UserIn):
    user = users_collection.find_one({'username':data.username})
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password"
        )
    hashed_pass = user['password']
    if not verify_password(data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password"
        )

    return {
        "access_token": create_access_token(user['username']),
        "refresh_token": create_refresh_token(user['username']),
    }



@routes.get('/profile', summary='Get details of currently logged in user', response_model=UserOut)
async def get_me(user = Depends(get_current_user)):
    return user


@routes.put('/update_profile', summary="Update user's information", response_model=UserOut)
async def update_profile(data: UserUpdate, user=Depends(get_current_user)):
    stored_user_model = UserUpdate(**user)
    update_data = data.dict(exclude_unset=True)
    update_user = stored_user_model.copy(update=update_data)
    user_data = jsonable_encoder(update_user)
    user = users_collection.update_one( {"_id": ObjectId(user['_id'])}, {"$set": user_data})

    return update_user