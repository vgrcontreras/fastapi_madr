from sqlalchemy import create_engine

from fastapi_madr.core.settings import Settings

engine = create_engine(Settings().DATABASE_URL)
