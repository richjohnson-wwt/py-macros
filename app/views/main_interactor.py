

import wx

from app import app_logging

logger = app_logging.get_app_logger(__name__)

class MainInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view


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


class RecipeInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view


class GoalInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view