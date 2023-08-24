
from app import app_logging

logger = app_logging.get_app_logger(__name__)

class MainPresenter:
    def __init__(self, daily, food, recipe, goal):
        self.daily = daily
        self.food = food
        self.recipe = recipe
        self.goal = goal

class DailyPresenter:
    def __init__(self, model, view, interactor):
        self.model = model
        self.view = view
        interactor.install(self, view)

class FoodPresenter:
    def __init__(self, model, view, interactor):
        self.model = model
        self.view = view
        interactor.install(self, view)
        model.register(self)

    def on_food_change(self, food_id):
        logger.info("Notified about Food selected: " + str(food_id))
        self.view.set_food(self.model.get_food(food_id))

class RecipePresenter:
    def __init__(self, model, view, interactor):
        self.model = model
        self.view = view
        interactor.install(self, view)
        model.register(self)

    def on_recipe_change(self, recipe_id):
        logger.info("Notified about Recipe selected: " + str(recipe_id))
        self.view.set_recipe(self.model.get_recipe(recipe_id))
        self.view.set_ingredients(self.model.get_ingredients(recipe_id))

class GoalPresenter:
    def __init__(self, model, view, interactor):
        self.model = model
        self.view = view
        interactor.install(self, view)