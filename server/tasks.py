from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Security
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List, Annotated, Union
from .authenticate import VerifyToken
from models.task import *
from server.helpers import *
from dotenv import dotenv_values
import json
import os

config = dotenv_values(".env")

auth = VerifyToken()

tasks_router = APIRouter()

@tasks_router.post("/users/{user_id}/tasks/create", response_description="Create a new task", response_model=TaskModel)
def create_task(request: Request, user_id: str, task: TaskModel = Body(...), auth_result: str = Security(auth.verify)):
    
    task = jsonable_encoder(task)
    task["user_id"] = user_id
    new_task = request.app.database[config["TASKS_COLLECTION"]].insert_one(task)
    created_task = request.app.database[config["TASKS_COLLECTION"]].find_one({
        "_id": new_task.inserted_id
    })

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_task)

@tasks_router.get("/users/{user_id}/tasks", response_description="Retrieve all tasks of a user", response_model=List[TaskModel])
def get_tasks(request: Request, user_id: str, auth_result: str = Security(auth.verify)):

    user_tasks = []
    for doc in list(request.app.database[config["TASKS_COLLECTION"]].find({"user_id": user_id})):
        user_tasks.append(doc)
    return JSONResponse(status_code=status.HTTP_200_OK, content=user_tasks)

@tasks_router.get("/users/{user_id}/tasks/{task_id}", response_description="Retrieve a single task of a user", response_model=TaskModel)
def get_task(request: Request, user_id: str, task_id: str, auth_result: str = Security(auth.verify)):

    retrieved_task = request.app.database[config["TASKS_COLLECTION"]].find_one({"_id": task_id})
    if retrieved_task is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=retrieved_task)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with ID {task_id} not found")

@tasks_router.put("/users/{user_id}/tasks/{task_id}", response_description="Update a single task of a user by task's id", response_model=UpdateTaskModel)
def update_task(request: Request, user_id: str, task_id: str, task: UpdateTaskModel = Body(...), auth_result: str = Security(auth.verify)):
    task = {k: v for k, v in task.dict().items() if v != ""}
    if len(task) >= 1:
        task["user_id"] = user_id
        update_result = request.app.database[config["TASKS_COLLECTION"]].update_one(
            {"_id": task_id}, {"$set": task}
        )

        if update_result.modified_count == 1:
            updated_task = request.app.database[config["TASKS_COLLECTION"]].find_one({"_id": task_id})
            if updated_task is not None:
                return JSONResponse(status_code=status.HTTP_201_CREATED, content=updated_task)

    existing_task = request.app.database[config["TASKS_COLLECTION"]].find_one({"_id": task_id})
    if existing_task is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=existing_task)

    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@tasks_router.delete("/users/{user_id}/tasks/{task_id}", response_description="Delete a task of a user by task's id")
def delete_task(request: Request, user_id: str, task_id: str, auth_result: str = Security(auth.verify)):
    delete_result = request.app.database[config["TASKS_COLLECTION"]].delete_one({"_id": task_id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


