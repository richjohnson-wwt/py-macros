
from app import app_logging

logger = app_logging.get_app_logger(__name__)

class DailyPresenter:
    def __init__(self, model, view, interactor):
        self.model = model
        self.view = view
        interactor.install(self, view)

    def post_init(self):
        pass

    def on_date_changed(self, new_date):
        logger.info("Date changed: %s", new_date)
        # self.view.set_date(event.GetDate())

    def on_add_activity(self):
        logger.info("Adding activity")
        pass

    def on_add_weight(self):
        logger.info("Adding weight")
        pass

    def on_add_food(self):
        logger.info("Adding food")
        pass

    def on_add_recipe(self):
        logger.info("Adding recipe")
        pass

    def on_add_one_off(self):
        logger.info("Adding one-off")
        pass


class FoodPresenter:
    def __init__(self, model, view, interactor, unit_model):
        self.model = model
        self.view = view
        self.unit_model = unit_model
        interactor.install(self, view)
        model.register('item_selected', self, self.update)

    def update(self, food_id):
        logger.info("Notified about Food selected: " + str(food_id))
        self.view.set_food(self.model.get_food(food_id), self.unit_model.get_units())

    def post_init(self):
        self.view.set_food(self.model.get_food(1), self.unit_model.get_units())


class RecipePresenter:
    def __init__(self, model, view, interactor):
        self.model = model
        self.view = view
        interactor.install(self, view)
        model.register('item_selected', self, self.update)

    def update(self, recipe_id):
        logger.info("Notified about Recipe selected: " + str(recipe_id))
        self.view.set_recipe(self.model.get_recipe(recipe_id))
        self.view.set_ingredients(self.model.get_ingredients(recipe_id))

    def post_init(self):
        self.view.set_recipe(self.model.get_recipe(3))
        self.view.set_ingredients(self.model.get_ingredients(3))


class GoalPresenter:
    def __init__(self, model, view, interactor):
        self.model = model
        self.view = view
        interactor.install(self, view)

    def post_init(self):
        self.view.set_goal(self.model.get_goal())