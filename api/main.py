from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from starlette.middleware.cors import CORSMiddleware
from api.utils.path_finding import find_path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h1>Hello, go to <a href='/docs'>docs</a> to view usage</h1>"


class Path(BaseModel):
    path: list[int]

@app.get("/find_labyrinth_path", response_model=Path)
async def find_labyrinth_path(start_location: int, end_location: int) -> Path:
    return {"path": find_path(start_location, end_location)}
