from os.path import dirname, abspath
from sys import path

path.insert(0, dirname(abspath(__file__)) + '/../')

from neverlose import Client
from neverlose.models.events import BalanceTransfer
from neverlose.models.events import ItemPurchase

from json import loads
from pathlib import Path

with open(Path(__file__).parent / 'config.json', 'r') as f:
    cfg = loads(f.read())

app = Client(**cfg)


@app.on_item_purchase()
async def my_purchase_handler(data: ItemPurchase):
    print(f'{data.username} just bought {data.item_id}')


@app.on_balance_transfer()
async def my_balance_transfer_handler(data: BalanceTransfer):
    print(f'{data.username} ty for {data.amount}')


if __name__ == '__main__':
    app.transfer_money(1.0, 'soufivw')
    app.give_market_item('soufivw', 'IS6raE')
    app.run_web()
