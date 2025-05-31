import os

from app.utils.alembic import import_all_models

import_all_models(
    "app.db.models",
    os.path.join(os.path.dirname(__file__), "..", "app", "db", "models"),
)
