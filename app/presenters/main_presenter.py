
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
    def __init__(self, model, view, interactor, food_model, macro_calculator):
        self.model = model
        self.view = view
        self.food_model = food_model
        self.macro_calculator = macro_calculator
        interactor.install(self, view)

    def post_init(self):
        todays_date = self.model.get_today_date()
        logger.info("Today's date: " + str(todays_date))
        # self.create_daily_food_if_not_exists(todays_date)
        self.on_date_changed(todays_date)

    def create_daily_food_if_not_exists(self, the_date):
        if self.model.does_date_exist(the_date):
            logger.info("Date already exists")
        else:
            logger.info("Creating new date: " + str(the_date))
            self.model.create_daily_food(the_date)

    def on_date_changed(self, new_date):
        logger.info("Date changed: %s", new_date)
        self.create_daily_food_if_not_exists(new_date)
        self.model.set_selected_date(new_date)
        self.load_view_from_model()

    def load_view_from_model(self):
        daily_food = self.model.get_daily_food()
        self.view.add_activity_text_ctrl.SetValue(str(daily_food.exercise))
        self.view.add_weight_text_ctrl.SetValue(str(daily_food.weight))
        self.view.reset_daily_multiplier(self.model.serving_increments, 5)
        food_list = self.model.get_xref_daily_foods(daily_food.daily_food_id)
        for f in food_list:
            logger.info("Food xref id: " + str(f.xref_id))
        self.view.set_daily_foods(food_list)

    def on_add_activity(self):
        logger.info("Adding activity")
        self.model.update_exercise_calorie_bonus(self.view.add_activity_text_ctrl.GetValue())

    def on_add_weight(self):
        logger.info("Adding weight")
        self.model.update_weight(self.view.add_weight_text_ctrl.GetValue())

    def on_add_food(self):
        logger.info("Adding food")
        daily_food = self.model.get_daily_food()
        food_item_to_add = self.food_model.get_food()
        multiplier = self.view.unit_combo_box.GetValue()
        calculated_macros = self.macro_calculator.calculate_food_macros(food_item_to_add, multiplier)
        self.model.add_xref_daily_food(
            daily_food.daily_food_id,
            food_item_to_add.name + " x " + str(multiplier),
            calculated_macros.fat_grams,
            calculated_macros.protein_grams,
            calculated_macros.carb_grams,
            calculated_macros.calories
        )
        self.load_view_from_model()

    def on_add_recipe(self):
        logger.info("Adding recipe")
        pass

    def on_add_one_off(self):
        logger.info("Adding one-off")
        pass

    def delete_food(self):
        logger.info("Deleting food")
        self.model.delete_xref_daily_food()

    def on_food_item_selected(self, xref_id):
        logger.debug("Food selected: " + xref_id)
        self.model.selected_xref_id = xref_id


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