from pathlib import Path

from fastapi import FastAPI

from app.plugins.i18n import init_i18n
from app.utils.core.router import load_routers

app = FastAPI()

# Load router from app.api package
api_dir = Path(__file__).parent / "api"
load_routers(app, api_dir)

# Initialize I18n
init_i18n()
