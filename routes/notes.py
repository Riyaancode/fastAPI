from fastapi import APIRouter, status
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Request, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.note import NoteModel
from config.db import conn
from schemas.note import notEntity, notEntityList

noteApp = APIRouter()

templates = Jinja2Templates(directory="templates")

@noteApp.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    todos = conn.test.todos.find()
    newtodos = []
    for todo in todos:
        newtodos.append({
            "id": str(todo["_id"]),  # Convert ObjectId to string
            "title": todo["title"],
            "description": todo["description"],
            "important": todo["important"]
        })
        print("newtodos", newtodos)
    # return templates.TemplateResponse("index.html", {"request": request, "newtodos": newtodos})
    return JSONResponse(status_code=status.HTTP_200_OK, content=newtodos)

# @noteApp.post("/")
# async def create_task(request: Request, note: notEntity):
#     print(note)
    # new_task_data = {
    #     "text": note.text
    # }
    # new_task = conn.test.todos.insert_one(dict(note))
    # print(new_task.inserted_id)
    # created_task = conn.test.todos.find_one(
    #     {"_id": new_task.inserted_id}
    # )
    # return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "test"})


@noteApp.post("/", response_description="Add new task")
async def create_task(request: Request, task: dict = Body(...)):
    try:
        # Convert the TaskModel instance to a dictionary
        task_dict = jsonable_encoder(task)

        # Insert the task data into MongoDB
        new_task = conn.test.todos.insert_one(task_dict)
        print(new_task)

        return JSONResponse(status_code=status.HTTP_201_CREATED, content=new_task)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
