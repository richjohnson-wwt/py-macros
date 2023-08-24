

from app import app_logging

logger = app_logging.get_app_logger(__name__)

class ExplorerPresenter:
    def __init__(self, food_list, recipe_list):
        self.food_list = food_list
        self.recipe_list = recipe_list

    def post_init(self):
        self.food_list.post_init()


class FoodListPresenter:
    def __init__(self, model, view, interactor):
        self.view = view
        self.model = model
        interactor.install(self, view)
        self.view.set_foods(self.model.get_foods())

    def on_food_item_selected(self, food_id):
        logger.info("Food list item selected: " + str(food_id))
        self.model.set_selected_food(food_id)


class RecipeListPresenter:
    def __init__(self, model, view, interactor):
        self.view = view
        self.model = model
        interactor.install(self, view)
        self.view.set_recipes(self.model.get_recipes())

    def on_recipe_item_selected(self, recipe_id):
        logger.info("Recipe list item selected: " + str(recipe_id))
        self.model.set_selected_recipe(recipe_id)
        