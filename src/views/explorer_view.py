
import wx

from src import app_logging

logger = app_logging.get_app_logger(__name__)

class ExplorerWindow(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.NB_TOP, size=(400, 600))

        self.food_page = FoodListWindow(self)
        self.AddPage(self.food_page, "Food")

        self.recipe_page = RecipeListWindow(self)
        self.AddPage(self.recipe_page, "Recipe")


class FoodListWindow(wx.Panel):
    def __init__(self, notebook):
        wx.Panel.__init__(self, notebook, id=wx.ID_ANY)
        top_sizer = wx.BoxSizer(wx.VERTICAL)

        self.search_text_ctrl = wx.SearchCtrl(self, id=wx.ID_ANY)
        search_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.search_text_ctrl.ShowCancelButton(True)
        search_sizer.Add(self.search_text_ctrl, 1, wx.EXPAND)
        top_sizer.Add(search_sizer, 0, wx.EXPAND)

        self.food_list_view = wx.ListView(self, wx.ID_ANY)
        self.food_list_view.InsertColumn(0, 'ID', width=70)
        self.food_list_view.InsertColumn(1, 'Name', width=360)
        list_sizer = wx.BoxSizer(wx.VERTICAL)
        list_sizer.Add(self.food_list_view, 1, wx.EXPAND)
        top_sizer.Add(list_sizer, 1, wx.EXPAND)

        self.SetSizer(top_sizer)

    def set_foods(self, foods):
        self.food_list_view.DeleteAllItems()
        row = 0
        for food in foods:
            self.food_list_view.InsertItem(row, str(food.id))
            self.food_list_view.SetItem(row, 1, food.name)
            row += 1


class RecipeListWindow(wx.Panel):
    def __init__(self, notebook, id=wx.ID_ANY):
        wx.Panel.__init__(self, notebook)
        top_sizer = wx.BoxSizer(wx.VERTICAL)
        self.recipe_list_view = wx.ListView(self, wx.ID_ANY)
        self.recipe_list_view.InsertColumn(0, 'ID2', width=70)
        self.recipe_list_view.InsertColumn(1, 'Name', width=360)

        list_box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        list_box_sizer.Add(self.recipe_list_view, 1, wx.EXPAND | wx.ALL)
        top_sizer.Add(list_box_sizer, 1, wx.EXPAND)
        self.SetSizer(top_sizer)

    def set_recipes(self, recipes):
        self.recipe_list_view.DeleteAllItems()
        row = 0
        for recipe in recipes:
            self.recipe_list_view.InsertItem(row, str(recipe.id))
            self.recipe_list_view.SetItem(row, 1, recipe.name)
            row += 1

