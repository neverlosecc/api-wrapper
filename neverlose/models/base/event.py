from pydantic import BaseModel


class BaseEvent(BaseModel):
    unique_id: int
    signature: str
