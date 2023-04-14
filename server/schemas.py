from typing import Optional
from pydantic import BaseModel


class UserIn(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str


class UserOut(BaseModel):
    user_id: int
    user_type: str

class Config:
    orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
