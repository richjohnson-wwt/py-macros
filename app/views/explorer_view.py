
import wx

from app import app_logging

logger = app_logging.get_app_logger(__name__)

class ExplorerWindow(wx.Panel):
    def __init__(self, parent, foot_list_view, recipe_list_view):
        wx.Panel.__init__(self, parent)
        self.macro_app_wx_frame = parent
        # self.notebook = wx.Notebook(parent, -1, style=wx.NB_TOP, size=(400, 600))
        self.food_list_view = foot_list_view
        self.recipe_list_view = recipe_list_view
        
    def create_explorer_notebook(self):
        # self.main_panel = wx.Panel(self.parent)
        logger.info("Creating explorer notebook")

        self.notebook = wx.Notebook(self.macro_app_wx_frame, -1, style=wx.NB_TOP, size=(400, 600))
        logger.info("Creating explorer notebook2")
        page1 = self.food_list_view.create_view(self.notebook)
        logger.info("Creating explorer notebook3")
        page2 = self.recipe_list_view.create_view(self.notebook)
        logger.info("Creating explorer notebook4")
        self.notebook.AddPage(page1, "Food")
        self.notebook.AddPage(page2, "Recipe")
        logger.info("Creating explorer notebook5")

        # self.food_list_view.create_view(self.notebook)
        # self.recipe_list_view.create_view(self.notebook)
        # parent.install_left(self)
        # _sizer = wx.BoxSizer(wx.VERTICAL)
        # _sizer.Add(self.notebook, 1, wx.EXPAND)
        # self.macro_app_wx_frame.SetSizerAndFit(_sizer)
        return self.notebook

    # def post_init(self):
    #     _sizer = wx.BoxSizer(wx.VERTICAL)
    #     _sizer.Add(self.notebook, 1, wx.EXPAND)
    #     self.main_panel.SetSizerAndFit(_sizer)

class FoodListView:
    def __init__(self):
        pass

    def create_view(self, notebook):
        # wx_panel = wx.Panel(notebook)
        # self.notebook = notebook
        top_sizer = wx.BoxSizer(wx.VERTICAL)
        tab_food = wx.Panel(notebook)

        search_text_ctrl = wx.SearchCtrl(tab_food)
        search_sizer = wx.BoxSizer(wx.HORIZONTAL)
        search_text_ctrl.ShowCancelButton(True)
        search_sizer.Add(search_text_ctrl, 1, wx.EXPAND)
        top_sizer.Add(search_sizer, 0, wx.EXPAND)

        self.food_list_view = wx.ListView(tab_food, -1, style=wx.LC_REPORT)
        self.food_list_view.InsertColumn(0, 'ID', width=70)
        self.food_list_view.InsertColumn(1, 'Name', width=360)
        list_sizer = wx.BoxSizer(wx.VERTICAL)
        list_sizer.Add(self.food_list_view, 1, wx.EXPAND)
        top_sizer.Add(list_sizer, 1, wx.EXPAND)

        tab_food.SetSizer(top_sizer)
        tab_food.Layout()
        notebook.AddPage(tab_food, "Foods")
        notebook.Layout()
        return tab_food

    def set_foods(self, foods):
        self.food_list_view.DeleteAllItems()
        row = 0
        for food in foods:
            self.food_list_view.InsertItem(row, str(food.id))
            self.food_list_view.SetItem(row, 1, food.name)
            row += 1


class RecipeListView:
    def __init__(self):
        pass

    def create_view(self, notebook):
        self.notebook = notebook
        top_sizer = wx.BoxSizer(wx.VERTICAL)
        tab_recipes = wx.Panel(notebook)
        self.recipe_list_view = wx.ListView(tab_recipes, -1, style=wx.LC_REPORT)
        self.recipe_list_view.InsertColumn(0, 'ID', width=70)
        self.recipe_list_view.InsertColumn(1, 'Name', width=360)

        list_box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        list_box_sizer.Add(self.recipe_list_view, 1, wx.EXPAND | wx.ALL)
        tab_recipes.SetSizer(list_box_sizer)
        self.notebook.AddPage(tab_recipes, "Recipes")
        return tab_recipes

    def set_recipes(self, recipes):
        self.recipe_list_view.DeleteAllItems()
        row = 0
        for recipe in recipes:
            self.recipe_list_view.InsertItem(row, str(recipe.id))
            self.recipe_list_view.SetItem(row, 1, recipe.name)
            row += 1

