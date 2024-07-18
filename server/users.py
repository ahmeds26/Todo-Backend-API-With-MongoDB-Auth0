from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBearer
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List, Annotated, Union, Optional
from .authenticate import VerifyToken
from models.user import *
from server.helpers import *
from dotenv import dotenv_values
import json
import os

config = dotenv_values(".env")

auth = VerifyToken()

users_router = APIRouter()


@users_router.post("/register", response_description="Create a new user", response_model=UserModel)
def register_user(request: Request, user: UserModel = Body(...)):

    # Check for already registered user
    if request.app.database[config["USERS_COLLECTION"]].find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create new user
    hashed_password = encrypt_password(user.password)
    user = jsonable_encoder(user)
    del user["password"]
    user["password_hash"] = hashed_password
    new_user = request.app.database[config["USERS_COLLECTION"]].insert_one(user)
    created_user = request.app.database[config["USERS_COLLECTION"]].find_one({
        "_id": new_user.inserted_id
    })
    del created_user["password_hash"]
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)

@users_router.post("/login", response_description="Login / Authenticate a user")
def login_user(request: Request, form_data: Annotated[OAuth2PasswordRequestForm, Depends()], auth_result: str = Security(auth.verify)):
    user = request.app.database[config["USERS_COLLECTION"]].find_one({
        "email": form_data.username
    })

    # Check for user's email is correct
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Check for user's password is correct
    hashed_pass = user['password_hash']
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )
    return auth_result


