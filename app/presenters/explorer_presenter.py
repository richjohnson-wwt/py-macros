

from app import app_logging

logger = app_logging.get_app_logger(__name__)


class FoodListPresenter:
    def __init__(self, model, view, interactor, explorer_model):
        self.view = view
        self.model = model
        # self.interactor = interactor
        interactor.install(self, self.view)
        self.explorer_model = explorer_model
        self.model.register('list_changed', self, self.food_list_changed)

    def on_food_item_selected(self, food_id):
        logger.info("Food list item selected: " + str(food_id))
        self.model.set_selected_food(food_id)
        self.explorer_model.selected_food_id = food_id

    def post_init(self):
        logger.info("post_init food list")
        foods = self.model.get_foods()
        logger.debug("foods size: %s", len(foods))
        self.view.set_foods(foods)
        # self.interactor.install(self, self.view)

    def food_list_changed(self):
        logger.info("Notified about Food list changed")
        self.view.set_foods(self.model.get_foods())

    def on_delete_food(self):
        logger.info("Deleting food")
        self.explorer_model.delete_food()

class RecipeListPresenter:
    def __init__(self, model, view, interactor, explorer_model):
        self.view = view
        self.model = model
        self.explorer_model = explorer_model
        # self.interactor = interactor
        interactor.install(self, self.view)
        
        self.model.register('list_changed', self, self.recipe_list_changed)

    def on_recipe_item_selected(self, recipe_id):
        logger.info("Recipe list item selected: " + str(recipe_id))
        self.model.set_selected_recipe(recipe_id)
        self.explorer_model.selected_recipe_id = recipe_id

    def post_init(self):
        logger.info("post_init recipe list")
        self.view.set_recipes(self.model.get_recipes())
        # self.interactor.install(self, self.view)

    def recipe_list_changed(self):
        logger.info("Notified about Recipe list changed")
        self.view.set_recipes(self.model.get_recipes())

    def on_delete_recipe(self):
        logger.info("Deleting recipe")
        self.explorer_model.delete_recipe()
        