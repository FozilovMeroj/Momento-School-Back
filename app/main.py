from pathlib import Path

from fastapi import FastAPI

from app.utils.router import load_routers

app = FastAPI()
api_dir = Path(__file__).parent / "api"
load_routers(app, api_dir)
