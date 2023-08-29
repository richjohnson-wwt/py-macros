
from daily_view import DailyWindow
from food_view import FoodWindow
from recipe_view import RecipeWindow
from goal_view import GoalWindow
import wx

from app import app_logging

logger = app_logging.get_app_logger(__name__)

class MainWindow(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.NB_TOP, size=(400, 600))
        self.macro_app_wx_frame = parent
        self.daily_page = DailyWindow(self)
        self.AddPage(self.daily_page, "Daily")

        self.food_page = FoodWindow(self)
        self.AddPage(self.food_page, "Food")

        self.recipe_page = RecipeWindow(self)
        self.AddPage(self.recipe_page, "Recipe")

        self.goal_page = GoalWindow(self)
        self.AddPage(self.goal_page, "Goal")


