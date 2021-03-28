from enum import IntEnum
from enum import auto
from enum import unique


@unique
class EEventType(IntEnum):
    BALANCE_TRANSFER = auto()
    ITEM_PURCHASE = auto()
