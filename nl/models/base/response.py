from pydantic import BaseModel


class BaseResponse(BaseModel):
    ok: bool
