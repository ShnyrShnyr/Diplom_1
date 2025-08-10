from Diplom_1.data import Data
from Diplom_1.praktikum.bun import Bun

class TestBun:

    def test_bun_get_name(self):
        bun = Bun(name=Data.BUN_NAME, price=Data.BUN_PRICE)
        assert bun.get_name() == Data.BUN_NAME, f'Проверяем, что название булки {Data.BUN_NAME}'

    def test_bun_get_price(self):
        bun = Bun(name=Data.BUN_NAME, price=Data.BUN_PRICE)
        assert bun.get_price() == Data.BUN_PRICE, f'Проверяем, что цена булки {Data.BUN_PRICE}'
