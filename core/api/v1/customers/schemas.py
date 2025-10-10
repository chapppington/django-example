from pydantic import BaseModel


class AuthInSchema(BaseModel):
    phone: str


class AuthOutSchema(BaseModel):
    message: str


class TokenOutSchema(BaseModel):
    token: str


class TokenInSchema(BaseModel):
    code: str
    phone: str
