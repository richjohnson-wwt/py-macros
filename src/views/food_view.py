
import wx
from layout_helper import create_label_with_text_sizer

class FoodWindow(wx.Panel):

    def __init__(self, notebook):
        wx.Panel.__init__(self, notebook, id=wx.ID_ANY)
        top_sizer = wx.BoxSizer(wx.VERTICAL)

        self.food_id_text_ctrl = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.Size(200, 20), wx.TE_READONLY)
        top_sizer.Add(create_label_with_text_sizer(self, "Food ID", self.food_id_text_ctrl), 0, wx.ALL, 10)

        self.food_name_text_ctrl = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(self, "Food Name", self.food_name_text_ctrl), 0, wx.ALL, 10)

        self.food_fat_text_ctrl = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(self, "Fat", self.food_fat_text_ctrl), 0, wx.ALL, 10)

        self.food_protein_text_ctrl = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(self, "Protein", self.food_protein_text_ctrl), 0, wx.ALL, 10)

        self.food_carbs_text_ctrl = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(self, "Carbs", self.food_carbs_text_ctrl), 0, wx.ALL, 10)

        self.food_calories_text_ctrl = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(self, "Calories", self.food_calories_text_ctrl), 0, wx.ALL, 10)

        self.food_quantity_text_ctrl = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(self, "Quantity", self.food_quantity_text_ctrl), 0, wx.ALL, 10)

        combo_box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.food_unit_combo_box = wx.ComboBox(self, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        combo_box_sizer.Add(wx.StaticText(self, -1, "Food Unit", wx.DefaultPosition, wx.Size(150, 20), wx.ALIGN_LEFT))
        combo_box_sizer.Add(self.food_unit_combo_box)
        top_sizer.Add(combo_box_sizer, 0, wx.ALL, 10)

        self.food_popularity_text_ctrl = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(self, "Popularity", self.food_popularity_text_ctrl), 0, wx.ALL, 10)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.apply_button = wx.Button(self, -1, "Apply")
        self.cancel_button = wx.Button(self, -1, "Cancel")
        self.new_button = wx.Button(self, -1, "New Food")

        button_sizer.Add(self.apply_button, 0, wx.ALL, 10)
        button_sizer.Add(self.cancel_button, 0, wx.ALL, 10)
        button_sizer.Add(self.new_button, 0, wx.ALL, 10)

        top_sizer.Add(button_sizer, 0, wx.ALL, 10)

        self.SetSizer(top_sizer)

    
    def set_food(self, food, units):
        self.food_id_text_ctrl.SetValue(str(food.id))
        self.food_name_text_ctrl.SetValue(str(food.name))
        self.food_fat_text_ctrl.SetValue(str(food.fat))
        self.food_protein_text_ctrl.SetValue(str(food.protein))
        self.food_carbs_text_ctrl.SetValue(str(food.carbs))
        self.food_calories_text_ctrl.SetValue(str(food.calories))
        self.food_quantity_text_ctrl.SetValue(str(food.quantity))
        self.food_unit_combo_box.Clear()
        for unit in units:
            self.food_unit_combo_box.Append(unit.name)
        self.food_unit_combo_box.SetSelection(food.unit_id - 1)
        self.food_popularity_text_ctrl.SetValue(str(food.popularity))


