from Diplom_1.praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


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

    def test_available_buns_expected_values(self, database, bun):
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