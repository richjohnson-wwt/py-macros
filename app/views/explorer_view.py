
import wx

class ExplorerWindow(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.main_panel = wx.Panel(self)
        self.notebook = wx.Notebook(self.main_panel, -1, style=wx.NB_TOP, size=(400, 600))
        parent.install_left(self)

    def notebook_ctrl(self):
        return self.notebook

    def post_init(self):
        _sizer = wx.BoxSizer(wx.VERTICAL)
        _sizer.Add(self.notebook, 1, wx.EXPAND)
        self.main_panel.SetSizerAndFit(_sizer)
    

class FoodListView(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)
        top_sizer = wx.BoxSizer(wx.VERTICAL)
        tab_food = wx.Panel(parent)

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
        parent.AddPage(tab_food, "Foods")
        parent.Layout()

    def set_foods(self, foods):
        self.food_list_view.DeleteAllItems()
        row = 0
        for food in foods:
            self.food_list_view.InsertItem(row, str(food.id))
            self.food_list_view.SetItem(row, 1, food.name)
            row += 1


class RecipeListView(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)
        top_sizer = wx.BoxSizer(wx.VERTICAL)
        tab_recipes = wx.Panel(parent)
        self.recipe_list_view = wx.ListView(tab_recipes, -1, style=wx.LC_REPORT)
        self.recipe_list_view.InsertColumn(0, 'ID', width=70)
        self.recipe_list_view.InsertColumn(1, 'Name', width=360)

        list_box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        list_box_sizer.Add(self.recipe_list_view, 1, wx.EXPAND | wx.ALL)
        tab_recipes.SetSizer(list_box_sizer)
        parent.AddPage(tab_recipes, "Recipes")

    def set_recipes(self, recipes):
        self.recipe_list_view.DeleteAllItems()
        row = 0
        for recipe in recipes:
            self.recipe_list_view.InsertItem(row, str(recipe.id))
            self.recipe_list_view.SetItem(row, 1, recipe.name)
            row += 1
