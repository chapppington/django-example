from pydantic import BaseModel


class PingResponseSchema(BaseModel):
    response: bool