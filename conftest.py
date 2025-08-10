import pytest
from Diplom_1.data import Data
from unittest.mock import Mock

from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.burger import Burger
from Diplom_1.praktikum.database import Database
from Diplom_1.praktikum.ingredient import Ingredient
from Diplom_1.praktikum.ingredient_types import INGREDIENT_TYPE_FILLING

@pytest.fixture
def bun():
    bun = Bun(Data.BUN_NAME,Data.BUN_PRICE)
    return bun

@pytest.fixture
def ingredient():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING,Data.INGREDIENT_NAME_1,Data.INGREDIENT_PRICE_1)
    return ingredient

@pytest.fixture
def bun_mock():
    mock_bun = Mock()
    mock_bun.name = Data.BUN_NAME
    mock_bun.price = Data.BUN_PRICE
    return mock_bun


@pytest.fixture
def ingredient_mock():
    mock_ingredient = Mock()
    mock_ingredient.ingredient_type = INGREDIENT_TYPE_FILLING
    mock_ingredient.name = Data.INGREDIENT_NAME_1
    mock_ingredient.price = Data.INGREDIENT_PRICE_1
    return mock_ingredient

@pytest.fixture
def burger_mock(mock_burger):
    mock_burger = Mock()
    mock_burger.bun.name = Data.BUN_NAME
    mock_burger.ingredients = [Data.INGREDIENT_NAME_1,Data.INGREDIENT_NAME_2]
    return mock_burger


@pytest.fixture
def create_burger_with_3_ingredients(bun_mock, ingredient_mock):
    burger = Burger()
    burger.set_buns(bun_mock)
    for i in range(3):
        ingredient_mock.get_name.return_value = f"{Data.INGREDIENT_NAME_1} {str(i)}"
        burger.add_ingredient(ingredient_mock)
    return burger

@pytest.fixture
def database():
    database = Database()
    return database

        