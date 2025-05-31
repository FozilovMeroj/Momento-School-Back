import os

from dotenv import load_dotenv

load_dotenv()

DEBUG: bool = os.getenv("DEBUG") == "True"
DATABASE_URL: str = os.getenv("DATABASE_URL", default="sqlite:///app.db")
