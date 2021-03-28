from typing import Optional

from ..base import BaseResponse


class Failed(BaseResponse):
    success = False
    error: Optional[str] = None
