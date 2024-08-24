from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class AccountSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class AccountDB(AccountSchema):
    id: int


class AccountPublic(BaseModel):
    id: int
    username: str
    email: str

class AccountList(BaseModel):
    users: list[AccountPublic]
