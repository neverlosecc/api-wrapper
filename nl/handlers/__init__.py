from ..enums import EEventType
from ..eventbus import Eventbus
from ..models import events
from ..models.base import BaseResponse


class Handlers(Eventbus):
    def mount_handlers(self):
        @self.web.post('/market/balance_transfer',
                       summary='Balance transfer event',
                       response_model=BaseResponse)
        async def _web_on_balance_transfer(form: events.BalanceTransfer):
            return await self.emit(EEventType.BALANCE_TRANSFER, form)

        @self.web.post('/market/item_purchase',
                       summary='Item purchase event',
                       response_model=BaseResponse)
        async def _web_on_item_purchase(form: events.ItemPurchase):
            return await self.emit(EEventType.ITEM_PURCHASE, form)
