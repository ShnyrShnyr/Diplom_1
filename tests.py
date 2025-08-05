from unittest.mock import Mock

from Diplom_1.praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import Data
import pytest

class TestBun:

    def test_bun_name(self, bun_mock):
        bun = Bun(name=Data.BUN_NAME, price=bun_mock.price)
        expected = bun.name
        assert expected == Data.BUN_NAME

    def test_bun_price(self, bun_mock):
        bun = Bun(name=bun_mock.name, price=Data.BUN_PRICE)
        expected = bun.price
        assert expected == Data.BUN_PRICE


    def test_bun_get_name(self, bun_mock):
        bun = Bun(name=bun_mock.name, price=bun_mock.price)
        expected = bun.get_name()
        assert expected == bun_mock.name, f'Проверяем, что название булки {bun_mock.name}'

    def test_bun_get_price(self, bun_mock):
        bun = Bun(name=bun_mock.name, price=bun_mock.price)
        expected = bun.get_price()
        assert expected == bun_mock.price, f'Проверяем, что цена булки {Data.BUN_PRICE}'

class TestBurger:

    def test_burger_set_buns(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        assert Data.BUN_NAME == burger.bun.get_name(), f'Проверяем, что {Data.BUN_NAME} добавлен в бургер'

    def test_burger_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert Data.INGREDIENT_NAME_1 == burger.ingredients[0].get_name(), f'Проверяем, что {Data.INGREDIENT_NAME_1} добавлен в бургер'
        
    def test_burger_move_ingredient(self, create_burger_with_3_ingredients):
        burger = create_burger_with_3_ingredients
        burger.move_ingredient(1,2)
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

class TestIngredient:
    @pytest.mark.parametrize(
        ['ingredient_type', 'name', 'price'],
        [
        (INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_NAME_1, Data.INGREDIENT_PRICE_1),
        (INGREDIENT_TYPE_FILLING, Data.INGREDIENT_NAME_2, Data.INGREDIENT_PRICE_2)
        ]
    )
    
    def test_ingredient_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type and ingredient.get_name() == name and ingredient.get_price() == price, f'Проверяем, что тип ингредиента {ingredient_type}, название - {name}, цена - {price} '

    def test_ingredient_get_name(self, ingredient):
        expected = ingredient.name
        assert expected == Data.INGREDIENT_NAME_1

class TestDatabase:
    def test_database_available_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == 3, 'Проверяем, что в базе доступно 3 булочки'

    def test_database_available_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6, 'Проверяем, что в базе доступно 6 ингредиентов'

    def test_available_buns_returns_list_of_bun_instances(self, database):
        buns = database.available_buns()
        assert isinstance(buns, list)

    def test_available_buns_expected_values(self, database):
        names = [bun.name for bun in database.available_buns()]
        assert names == ["black bun", "white bun", "red bun"]

    def test_available_price_expected_values (self, database):

        prices = [bun.price for bun in database.available_buns()]
        assert prices == [100, 200, 300]

    def test_available_ingredients_grouped_by_type(self, database):
        ingredients = database.available_ingredients()
        sauces = [i for i in ingredients if i.type == INGREDIENT_TYPE_SAUCE]
        fillings = [i for i in ingredients if i.type == INGREDIENT_TYPE_FILLING]

        assert len(sauces) == 3
        assert len(fillings) == 3

        sauce_names = sorted(i.name for i in sauces)
        filling_names = sorted(i.name for i in fillings)

        assert sauce_names == ["chili sauce", "hot sauce", "sour cream"]
        assert filling_names == ["cutlet", "dinosaur", "sausage"]