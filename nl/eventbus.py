from typing import Dict
from typing import List

from .enums import EEventType
from .models.base import BaseEvent
from .models.base import BaseResponse
from .models.responses import Failed
from .models.responses import Ok
from .scaffold import Scaffold
from .types import HANDLER
from .utils import signature


class Eventbus(Scaffold):
    _subscribed: Dict[EEventType, List[HANDLER]] = {}

    def subscribe(self, event):
        def decorator(fn: HANDLER):
            if event not in self._subscribed.keys():
                self._subscribed[event] = list()
            self._subscribed[event].append(fn)

            return fn

        return decorator

    async def emit(self, event: EEventType, data: BaseEvent) -> BaseResponse:
        if not signature.validate(data.dict(), self.secret):
            return Failed()

        if event not in self._subscribed.keys():
            return Ok()  # not really, but who cares ( FIXME? )
        if len(self._subscribed[event]) == 0:
            return Ok()  # not really, but who cares ( FIXME? )

        for handler in self._subscribed[event]:
            await handler(data)

        return Ok()

    def on_balance_transfer(self):
        return self.subscribe(EEventType.BALANCE_TRANSFER)

    def on_item_purchase(self):
        return self.subscribe(EEventType.ITEM_PURCHASE)
