from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from typing import Union
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
conn = MongoClient(
    "")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    todos = conn.test.todos.find()
    newtodos = []
    for todo in todos:
        newtodos.append({
            "id": todo["_id"],
            "text": todo["text"]
        })
        print("newtodos", newtodos)
    return templates.TemplateResponse("index.html", {"request": request, "newtodos": newtodos})
