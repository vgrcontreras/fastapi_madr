from datetime import datetime, timedelta

from jwt import encode
from pwdlib import PasswordHash
from zoneinfo import ZoneInfo

from fastapi_madr.core.settings import settings

password_hash = PasswordHash.recommended()


def get_password_hash(plain_password: str):
    return password_hash.hash(plain_password)


def get_password_verify(plain_password: str, hash_password: str):
    return password_hash.verify(plain_password, hash_password)


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({'exp': expire})

    encoded_jwt = encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )

    return encoded_jwt
