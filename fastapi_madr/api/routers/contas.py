from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi_madr.api.dependencies import SessionDep, get_session
from fastapi_madr.models import Account
from fastapi_madr.schemas.contas import AccountPublic, AccountSchema
from fastapi_madr.security import get_password_hash
from fastapi_madr.utils import sanitize

router = APIRouter()


@router.post('/', status_code=HTTPStatus.CREATED, response_model=AccountPublic)
def create_account(
    account: AccountSchema,
    session: SessionDep
):
    db_user = session.scalar(
        select(Account).where(
            (Account.username == account.username)
            | (Account.email == account.email)
        )
    )

    if db_user:
        if db_user.email == account.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='conta já consta no MADR'
            )

        if db_user.username == account.username:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='conta já consta no MADR'
            )

    db_user = Account(
        username=sanitize(account.username),
        email=account.email,
        password=get_password_hash(account.password)
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@router.put('/{user_id}', status_code=HTTPStatus.OK, )
def update_account(user_id: int, session: SessionDep):
    ...


@router.delete('/{user_id}', status_code=HTTPStatus.OK)
def delete_account():
    ...
