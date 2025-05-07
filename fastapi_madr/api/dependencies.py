from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from fastapi_madr.core.database import engine


def get_session():  # pragma: no cover
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
