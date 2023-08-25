
from app import app_logging

logger = app_logging.get_app_logger(__name__)

class MainPresenter:
    def __init__(self, model, view, interactor):
        self.model = model
        self.view = view
        interactor.install(self, view)

    def on_notebook_page_changed(self, page):
        logger.debug("Notebook page changed: %s", page)
        self.model.notify(page)

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
    def __init__(self, model, view, interactor, unit_model, main_model):
        self.model = model
        self.view = view
        self.unit_model = unit_model
        self.is_listening = False
        main_model.register(self)
        interactor.install(self, view)
        model.register('item_selected', self, self.update)

    def update(self):
        if self.is_listening:
            logger.info("Notified about Food selected")
            self.is_listening = False
            self.view.set_food(self.model.get_food(), self.unit_model.get_units())
            self.is_listening = True

    def post_init(self):
        self.view.set_food(self.model.get_food(), self.unit_model.get_units())
        self.view.apply_button.Enable(False)
        self.view.cancel_button.Enable(False)

    def notebook_page_change(self, message):
        logger.debug("FoodPresenter - Notebook page changed: %s", message)
        self.is_listening = True
        self.view.new_button.Enable(True)
        self.view.apply_button.Enable(False)
        self.view.cancel_button.Enable(False)

    def on_add_food(self):
        self.model.create_new_food()

    def on_apply_food(self):
        self.view.apply_button.Enable(False)
        self.view.new_button.Enable(True)
        self.view.cancel_button.Enable(False)
        unit_id = self.view.food_unit_combo_box.GetSelection() + 1
        logger.info("Unit selected: " + str(unit_id))
        self.model.update_food(
            self.view.food_name_text_ctrl.GetValue(),
            self.view.food_fat_text_ctrl.GetValue(),
            self.view.food_protein_text_ctrl.GetValue(),
            self.view.food_carbs_text_ctrl.GetValue(),
            self.view.food_calories_text_ctrl.GetValue(),
            self.view.food_quantity_text_ctrl.GetValue(),
            unit_id,
            self.view.food_popularity_text_ctrl.GetValue())

    def on_cancel_food(self):
        self.view.apply_button.Enable(False)
        self.view.new_button.Enable(True)
        self.view.cancel_button.Enable(False)
        self.view.set_food(self.model.get_food(1), self.unit_model.get_units())

    def on_food_changed(self):
        if self.is_listening:
            logger.debug("Food changed")
            self.view.apply_button.Enable(True)
            self.view.cancel_button.Enable(True)
        else:
            logger.debug("Not Listening")

class RecipePresenter:
    def __init__(self, model, view, interactor, unit_model, main_model, food_model):
        self.model = model
        self.view = view
        self.unit_model = unit_model
        self.food_model = food_model
        self.is_listening = False
        main_model.register(self)
        interactor.install(self, view)
        model.register('item_selected', self, self.update)

    def update(self):
        logger.info("Notified about Recipe selected")
        self.is_listening = False
        self.view.set_recipe(self.model.get_recipe())
        self.view.set_ingredients(self.model.get_ingredients())
        self.is_listening = True

    def post_init(self):
        self.view.set_recipe(self.model.get_recipe())
        self.view.set_ingredients(self.model.get_ingredients())

    def notebook_page_change(self, message):
        logger.debug("RecipePresenter - Notebook page changed: %s", message)
        self.is_listening = True
        self.view.new_button.Enable(True)
        self.view.apply_button.Enable(False)
        self.view.cancel_button.Enable(False)
        # set view with food selected in model

    def on_add_recipe(self):
        self.model.create_new_recipe()
        self.view.set_recipe(self.model.get_recipe())

    def on_add_ingredient(self):
        food = self.food_model.get_food()
        unit = self.unit_model.get_unit(food.unit_id)
        multiplier = self.view.ingredient_multiplier_text_ctrl.GetValue()
        self.view.append_ingredient(food, unit, multiplier)
        self.view.apply_button.Enable(True)
        self.view.cancel_button.Enable(True)

    def on_delete_ingredient(self):
        selected_index = self.view.ingredients_list_view.GetFirstSelected()
        if selected_index >= 0:
            self.view.ingredients_list_view.DeleteItem(selected_index)
        self.view.apply_button.Enable(True)
        self.view.cancel_button.Enable(True)

    def on_apply_recipe(self):
        self.view.apply_button.Enable(False)
        self.view.new_button.Enable(True)
        self.view.cancel_button.Enable(False)
        self.model.update_recipe(
            self.view.recipe_name_text_ctrl.GetValue(),
            self.view.recipe_description_text_ctrl.GetValue(),
            self.view.recipe_instructions_text_ctrl.GetValue(),
            self.view.recipe_url_text_ctrl.GetValue(),
            self.view.recipe_servings_text_ctrl.GetValue()
        )
        self.model.delete_ingredients()
        items = []
        for i in range(self.view.ingredients_list_view.GetItemCount()):
            item = []
            item.append(self.view.ingredients_list_view.GetItem(i, 0).GetText())
            item.append(self.view.ingredients_list_view.GetItem(i, 3).GetText())
            item.append(self.view.ingredients_list_view.GetItem(i, 4).GetText())
            items.append(item)
        for item in items:
            unit = self.unit_model.get_unit_by_name(item[1])
            self.model.add_recipe_ingredient(item[0], item[2], unit.unit_id)

    def on_cancel_recipe(self):
        self.view.apply_button.Enable(False)
        self.view.new_button.Enable(True)
        self.view.cancel_button.Enable(False)

    def on_recipe_changed(self):
        if self.is_listening:
            logger.debug("Recipe changed")
            self.view.apply_button.Enable(True)
            self.view.cancel_button.Enable(True)
        else:
            logger.debug("Not Listening")

    def on_ingredients_changed(self):
        if self.is_listening:
            logger.debug("Ingredients changed")
            self.view.apply_button.Enable(True)
            self.view.cancel_button.Enable(True)
        else:
            logger.debug("Not Listening")


class GoalPresenter:
    def __init__(self, model, view, interactor):
        self.model = model
        self.view = view
        interactor.install(self, view)

    def post_init(self):
        self.view.set_goal(self.model.get_goal())