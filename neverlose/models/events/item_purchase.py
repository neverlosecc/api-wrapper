from ..base.event import BaseEvent


class ItemPurchase(BaseEvent):
    amount: float
    username: str
    item_id: str
