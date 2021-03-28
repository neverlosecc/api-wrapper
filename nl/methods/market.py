from typing import Union

from ..requests import Requests


class Market(Requests):

    def give_market_item(self, username: str, item_id: str) -> bool:
        """
        Give a market item to [username]
        :param username: user who'll receive item for free
        :param item_id: market item id, can be extracted from url /item on site
        :return: success - true or false
        """
        return self._api_request('market/give-for-free',
                                 username=username, code=item_id)

    def transfer_money(self, amount: Union[float, int], username: str) -> bool:
        """
        Transfer market balance from account to [username]'s account
        :param amount: amount of $$$ to be transferred
        :param username: user who'll receive balance
        :return: success - true or false
        """
        amount = amount if isinstance(amount, float) else float(amount)
        return self._api_request('market/transfer-money',
                                 amount=amount, username=username)
