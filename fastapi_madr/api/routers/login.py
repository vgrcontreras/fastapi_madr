from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select

from fastapi_madr.api.dependencies import SessionDep
from fastapi_madr.models import Account
from fastapi_madr.schemas.base import Token
from fastapi_madr.security import create_access_token, get_password_verify

router = APIRouter()


@router.post('/', status_code=HTTPStatus.OK, response_model=Token)
def login_for_access_token(
    session: SessionDep,
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user_db = session.scalar(
        select(Account).where(
            Account.email == form_data.username
        )
    )

    if not user_db:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Incorrect email or password',
        )

    if not get_password_verify(form_data.password, user_db.password):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Incorrect email or password',
        )

    access_token = create_access_token(
        data={
            'sub': user_db.email,
        }
    )

    return {'access_token': access_token, 'token_type': 'bearer'}
