from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from api.utils.path_finding import find_path

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h1>Hello, go to <a href='/docs'>docs</a> to view usage</h1>"


@app.get("/find_labyrinth_path")
async def find_labyrinth_path(start_location: int, end_location: int) -> dict:
    return {"path": find_path(start_location, end_location)}
