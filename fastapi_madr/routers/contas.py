from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from fastapi_madr.schemas import AccountPublic, AccountSchema
from fastapi_madr.models import Account
from fastapi_madr.database import get_session
from fastapi_madr.utils import sanitize
from fastapi_madr.security import get_password_hash

router = APIRouter(prefix='/contas', tags=['contas'])


@router.post('/', status_code=HTTPStatus.CREATED, response_model=AccountPublic)
def create_account(
    account: AccountSchema,
    session: Session = Depends(get_session)   
):
    db_user = session.scalar(
        select(Account).where(
            (Account.username == account.username) | (Account.email == account.email)
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
        username = sanitize(account.username),
        email = account.email,
        password = get_password_hash(account.password)
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user

@router.put('/')
def update_account():
    ...


@router.delete('/')
def delete_account():
    ...
