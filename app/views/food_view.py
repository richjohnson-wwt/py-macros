
import wx
from layout_helper import create_label_with_text_sizer

class FoodWindow(wx.Notebook):

    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)
        top_panel = wx.Panel(parent)
        top_sizer = wx.BoxSizer(wx.VERTICAL)

        self.food_id_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20), wx.TE_READONLY)
        top_sizer.Add(create_label_with_text_sizer(top_panel, "Food ID", self.food_id_text_ctrl), 0, wx.ALL, 10)

        self.food_name_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(top_panel, "Food Name", self.food_name_text_ctrl), 0, wx.ALL, 10)

        self.food_fat_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(top_panel, "Fat", self.food_fat_text_ctrl), 0, wx.ALL, 10)

        self.food_protein_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(top_panel, "Protein", self.food_protein_text_ctrl), 0, wx.ALL, 10)

        self.food_carbs_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(top_panel, "Carbs", self.food_carbs_text_ctrl), 0, wx.ALL, 10)

        self.food_calories_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(top_panel, "Calories", self.food_calories_text_ctrl), 0, wx.ALL, 10)

        self.food_quantity_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(top_panel, "Quantity", self.food_quantity_text_ctrl), 0, wx.ALL, 10)

        combo_box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.food_unit_combo_box = wx.ComboBox(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        combo_box_sizer.Add(wx.StaticText(top_panel, -1, "Food Unit", wx.DefaultPosition, wx.Size(150, 20), wx.ALIGN_LEFT))
        combo_box_sizer.Add(self.food_unit_combo_box)
        top_sizer.Add(combo_box_sizer, 0, wx.ALL, 10)

        self.food_popularity_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(top_panel, "Popularity", self.food_popularity_text_ctrl), 0, wx.ALL, 10)

        top_panel.SetSizer(top_sizer)
        parent.AddPage(top_panel, "Food")
    
    def set_food(self, food, units):
        self.food_id_text_ctrl.SetValue(str(food.id))
        self.food_name_text_ctrl.SetValue(str(food.name))
        self.food_fat_text_ctrl.SetValue(str(food.fat))
        self.food_protein_text_ctrl.SetValue(str(food.protein))
        self.food_carbs_text_ctrl.SetValue(str(food.carbs))
        self.food_calories_text_ctrl.SetValue(str(food.calories))
        self.food_quantity_text_ctrl.SetValue(str(food.quantity))
        # self.food_unit_id_text_ctrl.SetValue(str(food.unit_id))
        self.food_unit_combo_box.Clear()
        for unit in units:
            self.food_unit_combo_box.Append(unit.name)
        self.food_unit_combo_box.SetSelection(food.unit_id - 1)
        self.food_popularity_text_ctrl.SetValue(str(food.popularity))


