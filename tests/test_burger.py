from unittest.mock import Mock
from Diplom_1.data import Data
from Diplom_1.praktikum.burger import Burger
from Diplom_1.praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_burger_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert (Data.BUN_NAME == burger.bun.name and Data.BUN_PRICE == burger.bun.price), f'Проверяем, что {Data.BUN_NAME} добавлен в бургер по цене булки {Data.BUN_PRICE}'

    def test_burger_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert Data.INGREDIENT_NAME_1 == burger.ingredients[0].get_name(), f'Проверяем, что {Data.INGREDIENT_NAME_1} добавлен в бургер'

    def test_burger_move_ingredient(self, create_burger_with_3_ingredients):
        burger = create_burger_with_3_ingredients
        burger.move_ingredient(1 ,2)
        assert burger.ingredients[1].get_name() == f'{Data.INGREDIENT_NAME_1} 2', "Проверяем, что ингредиент 3 теперь на 2 месте"

    def test_burger_remove_ingredient(self, create_burger_with_3_ingredients):
        burger = create_burger_with_3_ingredients
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 2, 'Проверяем, что в бургере теперь 2 ингредиента'

    def test_burger_get_price(self, bun_mock, ingredient_mock):
        bun_mock.get_price.return_value = 100.00
        ingredient_mock.get_price.return_value = 100.00
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == 300.00, 'Проверяем, что цена бургера = 2 цены булочки + цена ингредиентов'

    def test_burger_get_receipt(self, bun_mock, ingredient_mock):
        bun_mock.get_name.return_value = Data.BUN_NAME
        ingredient_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient_mock.get_name.return_value = Data.INGREDIENT_NAME_1
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        burger.get_price = Mock(return_value=Data.BURGER_PRICE)
        receipt = burger.get_receipt()
        receipt_expected = f'(==== {Data.BUN_NAME} ====)\n= {INGREDIENT_TYPE_SAUCE.lower()} {Data.INGREDIENT_NAME_1} =\n(==== {Data.BUN_NAME} ====)\n\nPrice: {Data.BURGER_PRICE}'
        print(receipt)
        print(receipt_expected)
        assert receipt == receipt_expected

