from fastapi import FastAPI

from fastapi_madr.routers import contas
from fastapi_madr.schemas import Message

app = FastAPI()

app.include_router(contas.router)


@app.get('/', response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}
