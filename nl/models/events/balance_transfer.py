from ..base.event import BaseEvent


class BalanceTransfer(BaseEvent):
    amount: float
    username: str
