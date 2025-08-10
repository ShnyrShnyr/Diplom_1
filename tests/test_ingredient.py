import pytest

from Diplom_1.data import Data
from Diplom_1.praktikum.ingredient import Ingredient
from Diplom_1.praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


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
