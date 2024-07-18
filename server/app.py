from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, JSONResponse, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from server.users import users_router as UserRouter
from server.tasks import tasks_router as TaskRouter
from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")

description = """
TODO Backend API.. 🚀

## Users:

You can do the following:

* **Create users**
* **Login with user's credentials**

## Tasks:

You can do the following:

* **Create a task for a specific user**
* **Read all tasks of a specific user**
* **Read a single task of a specific user**
* **Update a single task of a specific user**
* **Delete a single task of a specific user**
"""

app = FastAPI(
    title="TODO APP API",
    description=description,
    summary="Implementation of a Todo API Assignment",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Ahmed Saeed",
        "url": "http://ahmed.example.com/contact/",
        "email": "ahmed@example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },
)

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGO_ATLAS_URI"])
    app.database = app.mongodb_client[config["DATABASE_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.database.drop_collection(config["USERS_COLLECTION"])
    app.database.drop_collection(config["TASKS_COLLECTION"])
    app.mongodb_client.close()
    

app.include_router(UserRouter, tags=["Users"], prefix="/api")
app.include_router(TaskRouter, tags=["Tasks"], prefix="/api")


@app.get("/api", tags=["Root"])
async def root(request: Request):
    response = """
                <html>
                    <head>
                        <title>Todo API</title>
                    </head>
                    <body>
                        <h1>Welcome to Todo APP Home API</h1>
                        <p>If you are a new user please <strong>Register</strong> or if you are already registered please <strong>Login</strong></p>
                    </body>
                </html>
               """
    return Response(status_code=status.HTTP_200_OK, content=response, media_type="text/html")