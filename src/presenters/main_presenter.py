from datetime import datetime, timedelta
import pandas as pd
from src import app_logging

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
    def __init__(self, model, view, interactor, food_model, recipe_model, goal_model, macro_calculator):
        self.model = model
        self.view = view
        self.food_model = food_model
        self.recipe_model = recipe_model
        self.goal_model = goal_model
        self.macro_calculator = macro_calculator
        interactor.install(self, view)

    def post_init(self):
        todays_date = self.model.get_today_date()
        logger.debug("Today's date: " + str(todays_date))
        self.on_date_changed(todays_date)

    def create_daily_food_if_not_exists(self, the_date):
        if self.model.does_date_exist(the_date):
            logger.debug("Date already exists")
        else:
            logger.debug("Creating new date: " + str(the_date))
            self.model.create_daily_food(the_date)

    def on_date_changed(self, new_date):
        logger.debug("Date changed: %s", new_date)
        self.create_daily_food_if_not_exists(new_date)
        self.model.set_selected_date(new_date)
        self.load_view_from_model()

    def load_view_from_model(self):
        daily_food = self.model.get_daily_food()
        self.view.add_activity_text_ctrl.SetValue(str(daily_food.exercise))
        self.view.add_weight_text_ctrl.SetValue(str(daily_food.weight))
        self.view.reset_daily_multiplier(self.model.serving_increments, 5)
        food_list = self.model.get_xref_daily_foods(daily_food.daily_food_id)
        for food in food_list:
            logger.debug("Carb: " + str(food.carbs))
        self.view.set_daily_foods(food_list)
        self.load_totals()

    def load_totals(self):
        bonus_calories = self.view.add_activity_text_ctrl.GetValue()
        goal = self.goal_model.get_goal()
        goal_fat_grams = self.macro_calculator.get_goal_fat_grams(goal, bonus_calories)
        goal_protein_grams = self.macro_calculator.get_goal_protein_grams(goal, bonus_calories)
        goal_carb_grams = self.macro_calculator.get_goal_carb_grams(goal, bonus_calories)
        goal_calories = self.macro_calculator.get_goal_calories(goal, bonus_calories)

        totals_list = self.model.get_totals(bonus_calories, goal, goal_fat_grams, goal_protein_grams, goal_carb_grams, goal_calories)
        self.view.set_daily_totals(totals_list)

    def on_add_activity(self):
        logger.debug("Adding activity")
        self.model.update_exercise_calorie_bonus(self.view.add_activity_text_ctrl.GetValue())

    def on_add_weight(self):
        logger.debug("Adding weight")
        self.model.update_weight(self.view.add_weight_text_ctrl.GetValue())

    def on_add_food(self):
        logger.debug("Adding food")
        daily_food = self.model.get_daily_food()
        food_item_to_add = self.food_model.get_food()
        multiplier = self.view.unit_combo_box.GetValue()
        calculated_macros = self.macro_calculator.calculate_food_macros(food_item_to_add, multiplier)
        self.model.add_xref_daily_food(
            daily_food.daily_food_id,
            food_item_to_add.name + " x " + str(multiplier),
            calculated_macros.fat_grams,
            calculated_macros.protein_grams,
            calculated_macros.carbs_grams,
            calculated_macros.calories
        )
        self.food_model.bump_popularity()
        self.load_view_from_model()

    def on_add_recipe(self):
        logger.debug("Adding recipe")
        daily_food = self.model.get_daily_food()
        recipe = self.recipe_model.get_recipe()
        ingredients = self.recipe_model.get_ingredients()
        multiplier = self.view.unit_combo_box.GetValue()
        calculated_macros = self.macro_calculator.calculate_recipe_macros(recipe.servings, ingredients, multiplier)
        self.model.add_xref_daily_food(
            daily_food.daily_food_id,
            recipe.name + " x " + str(multiplier),
            int(calculated_macros.fat_grams),
            int(calculated_macros.protein_grams),
            int(calculated_macros.carb_grams),
            int(calculated_macros.calories)
        )
        self.load_view_from_model()

    def on_add_one_off(self):
        logger.debug("Adding one-off")
        # prompt user with the one-off dialog
        values = self.view.prompt_user_for_one_off()
        if values is not None:
            daily_food = self.model.get_daily_food()
            self.model.add_xref_daily_food(daily_food.daily_food_id, values[0], values[1], values[2], values[3], values[4])
        self.load_view_from_model()
 
    def delete_food(self):
        logger.debug("Deleting food")
        self.model.delete_xref_daily_food()
        self.load_view_from_model()

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
            logger.debug("Notified about Food selected")
            self.is_listening = False
            self.view.set_food(self.model.get_food(), self.unit_model.get_units())
            self.is_listening = True
        else:
            logger.debug("Notified about Food selected but not listening")

    def post_init(self):
        logger.debug("Post init FoodPresenter")
        self.view.set_food(self.model.get_food(), self.unit_model.get_units())
        self.view.apply_button.Enable(False)
        self.view.cancel_button.Enable(False)
        self.is_listening = True

    def notebook_page_change(self, message):
        logger.debug("FoodPresenter - Notebook page changed: %s", message)
        self.view.new_button.Enable(True)
        self.view.apply_button.Enable(False)
        self.view.cancel_button.Enable(False)

    def on_add_food(self):
        logger.debug("Adding food")
        self.model.create_new_food()
        self.update()

    def on_apply_food(self):
        self.view.apply_button.Enable(False)
        self.view.new_button.Enable(True)
        self.view.cancel_button.Enable(False)
        unit_id = self.view.food_unit_combo_box.GetSelection() + 1
        logger.debug("Unit selected: " + str(unit_id))
        self.model.update_food(
            self.view.food_name_text_ctrl.GetValue(),
            self.view.food_fat_text_ctrl.GetValue(),
            self.view.food_protein_text_ctrl.GetValue(),
            self.view.food_carbs_text_ctrl.GetValue(),
            self.view.food_calories_text_ctrl.GetValue(),
            self.view.food_quantity_text_ctrl.GetValue(),
            unit_id,
            self.view.food_popularity_text_ctrl.GetValue())
        self.update()

    def on_cancel_food(self):
        self.view.apply_button.Enable(False)
        self.view.new_button.Enable(True)
        self.view.cancel_button.Enable(False)
        self.update()

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
        logger.debug("Notified about Recipe selected")
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

    def on_add_recipe(self):
        self.model.create_new_recipe()
        self.view.set_recipe(self.model.get_recipe())
        self.view.set_ingredients([])
        self.update()

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
        self.update()

    def on_cancel_recipe(self):
        self.view.apply_button.Enable(False)
        self.view.new_button.Enable(True)
        self.view.cancel_button.Enable(False)
        self.update()

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


class ChartPresenter:
    def __init__(self, daily_model, goal_model, view, interactor):
        self.daily_model = daily_model
        self.goal_model = goal_model
        self.view = view
        interactor.install(self, view)
        self.populate_chart_data()

    def populate_chart_data(self):
        end_date = self.daily_model.get_today_date()
        start_date = self.goal_model.get_goal().start_date

        dt_start = datetime.strptime(start_date, "%Y-%m-%d")
        dt_end = datetime.strptime(end_date, "%Y-%m-%d")
        days_elapsed = dt_end - dt_start

        logger.debug("Days Elapsed: " + str(days_elapsed.days))
        logger.debug("Date range is: " + str(start_date) + " to " + str(end_date))
        daily_foods_by_date_range = self.daily_model.get_daily_food_by_date_range(start_date, end_date)
        logger.debug("Daily foods by date range: " + str(len(daily_foods_by_date_range)))
        weights = []
        x_axis = []
        x_value = 1
        for daily_food in daily_foods_by_date_range:
            if daily_food.weight > 0:
                weights.append(daily_food.weight)
                x_axis.append(x_value)
                x_value += 1
        weights.append(165)
        x_axis.append(x_value + 1)
        self.view.draw_chart(x_axis, weights)