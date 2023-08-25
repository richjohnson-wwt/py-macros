

import wx

from app import app_logging

logger = app_logging.get_app_logger(__name__)

class MainInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view
        self.view.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_notebook_page_changed)

    def on_notebook_page_changed(self, event):
        logger.debug("Notebook page changed: %s", event.GetSelection())
        self.presenter.on_notebook_page_changed(event.GetSelection())


class DailyInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view
        self.view.calendar_ctrl.Bind(wx.adv.EVT_CALENDAR_SEL_CHANGED, self.on_date_changed)
        self.view.add_activity_button.Bind(wx.EVT_BUTTON, self.on_add_activity)
        self.view.add_weight_button.Bind(wx.EVT_BUTTON, self.on_add_weight)
        self.view.add_food_button.Bind(wx.EVT_BUTTON, self.on_add_food)
        self.view.add_recipe_button.Bind(wx.EVT_BUTTON, self.on_add_recipe)
        self.view.add_one_off_button.Bind(wx.EVT_BUTTON, self.on_add_one_off)

    def on_date_changed(self, event):
        logger.info("Date changed: %s", event.GetDate())
        self.presenter.on_date_changed(event.GetDate())

    def on_add_activity(self, event):
        self.presenter.on_add_activity()

    def on_add_weight(self, event):
        self.presenter.on_add_weight()

    def on_add_food(self, event):
        self.presenter.on_add_food()

    def on_add_recipe(self, event):
        self.presenter.on_add_recipe()

    def on_add_one_off(self, event):
        self.presenter.on_add_one_off()

class FoodInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view
        self.view.new_button.Bind(wx.EVT_BUTTON, self.on_add_food)
        self.view.apply_button.Bind(wx.EVT_BUTTON, self.on_apply_food)
        self.view.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel_food)
        self.view.food_name_text_ctrl.Bind(wx.EVT_TEXT, self.on_food_changed)
        self.view.food_fat_text_ctrl.Bind(wx.EVT_TEXT, self.on_food_changed)
        self.view.food_carbs_text_ctrl.Bind(wx.EVT_TEXT, self.on_food_changed)
        self.view.food_protein_text_ctrl.Bind(wx.EVT_TEXT, self.on_food_changed)
        self.view.food_calories_text_ctrl.Bind(wx.EVT_TEXT, self.on_food_changed)
        self.view.food_quantity_text_ctrl.Bind(wx.EVT_TEXT, self.on_food_changed)
        self.view.food_popularity_text_ctrl.Bind(wx.EVT_TEXT, self.on_food_changed)
        self.view.food_unit_combo_box.Bind(wx.EVT_COMBOBOX, self.on_food_changed)

    def on_food_changed(self, event):
        if self.presenter.is_listening:
            logger.debug("Food changed: %s", event.GetString())
            self.presenter.on_food_changed()
        else:
            logger.debug("Not listening")

    def on_add_food(self, event):
        self.presenter.on_add_food()

    def on_apply_food(self, event):
        self.presenter.on_apply_food()

    def on_cancel_food(self, event):
        self.presenter.on_cancel_food()


class RecipeInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view
        self.view.new_button.Bind(wx.EVT_BUTTON, self.on_add_recipe)
        self.view.apply_button.Bind(wx.EVT_BUTTON, self.on_apply_recipe)
        self.view.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel_recipe)
        self.view.recipe_name_text_ctrl.Bind(wx.EVT_TEXT, self.on_recipe_changed)
        self.view.recipe_description_text_ctrl.Bind(wx.EVT_TEXT, self.on_recipe_changed)
        self.view.recipe_instructions_text_ctrl.Bind(wx.EVT_TEXT, self.on_recipe_changed)
        self.view.recipe_url_text_ctrl.Bind(wx.EVT_TEXT, self.on_recipe_changed)
        self.view.recipe_servings_text_ctrl.Bind(wx.EVT_TEXT, self.on_recipe_changed)
        self.view.add_food_with_multiplier_button.Bind(wx.EVT_BUTTON, self.on_add_ingredient)
        self.view.ingredients_list_view.Bind(wx.EVT_KEY_DOWN, self.on_key_down)


    def on_key_down(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            self.presenter.on_delete_ingredient()

    def on_add_recipe(self, event):
        self.presenter.on_add_recipe()

    def on_add_ingredient(self, event):
        self.presenter.on_add_ingredient()

    def on_apply_recipe(self, event):
        self.presenter.on_apply_recipe()

    def on_cancel_recipe(self, event):
        self.presenter.on_cancel_recipe()

    def on_recipe_changed(self, event):
        if self.presenter.is_listening:
            logger.debug("Recipe changed: %s", event.GetString())
            self.presenter.on_recipe_changed()
        else:
            logger.debug("Not listening")

    def on_ingredients_changed(self, event):
        if self.presenter.is_listening:
            logger.debug("Ingredients changed: %s", event.GetString())
            self.presenter.on_ingredients_changed()
        else:
            logger.debug("Not listening")

class GoalInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view