
import wx

class RecipeWindow(wx.Notebook):

    def create_label_with_text_sizer(self, panel, label_text, text_ctrl):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(wx.StaticText(panel, -1, label_text, wx.DefaultPosition, wx.Size(100, 20), wx.ALIGN_LEFT))
        sizer.Add(text_ctrl, wx.ALIGN_LEFT)
        return sizer

    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)
        top_panel = wx.Panel(parent)
        top_sizer = wx.BoxSizer(wx.VERTICAL)

        self.recipe_id_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(self.create_label_with_text_sizer(top_panel, "ID", self.recipe_id_text_ctrl), 0, wx.ALL, 10)

        self.recipe_name_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(self.create_label_with_text_sizer(top_panel, "Name", self.recipe_name_text_ctrl), 0, wx.ALL, 10)

        self.recipe_description_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(self.create_label_with_text_sizer(top_panel, "Description", self.recipe_description_text_ctrl), 0, wx.ALL, 10)

        self.recipe_instructions_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(self.create_label_with_text_sizer(top_panel, "Instructions", self.recipe_instructions_text_ctrl), 0, wx.ALL, 10)

        self.recipe_url_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(self.create_label_with_text_sizer(top_panel, "URL", self.recipe_url_text_ctrl), 0, wx.ALL, 10)

        self.recipe_servings_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(self.create_label_with_text_sizer(top_panel, "Servings", self.recipe_servings_text_ctrl), 0, wx.ALL, 10)

        self.ingredients_list_view = wx.ListView(top_panel, -1, style=wx.LC_REPORT)
        list_sizer = wx.BoxSizer(wx.VERTICAL)
        self.ingredients_list_view.AppendColumn("ID")
        self.ingredients_list_view.AppendColumn("Name")
        self.ingredients_list_view.AppendColumn("Quantity")
        self.ingredients_list_view.AppendColumn("Unit")
        self.ingredients_list_view.AppendColumn("Multiplier")
        self.ingredients_list_view.SetColumnWidth(0, 50)
        self.ingredients_list_view.SetColumnWidth(1, 320)
        self.ingredients_list_view.SetColumnWidth(2, 50)
        self.ingredients_list_view.SetColumnWidth(3, 50)
        self.ingredients_list_view.SetColumnWidth(4, 50)
        list_sizer.Add(self.ingredients_list_view, 1, wx.EXPAND, 10)

        top_sizer.Add(list_sizer, 1, wx.EXPAND, 10)

        top_panel.SetSizer(top_sizer)

        parent.AddPage(top_panel, "Recipe")

    def set_recipe(self, recipe):
        self.recipe_id_text_ctrl.SetValue(str(recipe.id))
        self.recipe_name_text_ctrl.SetValue(str(recipe.name))
        self.recipe_description_text_ctrl.SetValue(str(recipe.description))
        self.recipe_instructions_text_ctrl.SetValue(str(recipe.instructions))
        self.recipe_url_text_ctrl.SetValue(str(recipe.url))
        self.recipe_servings_text_ctrl.SetValue(str(recipe.servings))

    def set_ingredients(self, ingredients):
        self.ingredients_list_view.DeleteAllItems()
        row = 0
        for ingredient in ingredients:
            self.ingredients_list_view.InsertItem(row, str(ingredient.food.id))
            self.ingredients_list_view.SetItem(row, 1, str(ingredient.food.name))
            self.ingredients_list_view.SetItem(row, 2, str(ingredient.food.quantity))
            self.ingredients_list_view.SetItem(row, 3, str(ingredient.unit.name))
            self.ingredients_list_view.SetItem(row, 4, str(ingredient.unit_multiplier))
            row += 1


        