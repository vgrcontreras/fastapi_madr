from fastapi import FastAPI

from fastapi_madr.api.routers import contas, login
from fastapi_madr.schemas.base import Message

app = FastAPI()

app.include_router(contas.router, prefix='/contas', tags=['contas'])
app.include_router(login.router, prefix='/token', tags=['token'])


@app.get('/', response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}
