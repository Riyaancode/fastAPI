from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.notes import noteApp


app = FastAPI()
app.include_router(noteApp)

app.mount("/static", StaticFiles(directory="static"), name="static")