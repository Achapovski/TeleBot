from pydantic import BaseModel


class Bot(BaseModel):
    token: str
