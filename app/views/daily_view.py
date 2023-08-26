

import wx
import wx.adv

from layout_helper import create_label_with_text_sizer

from app import app_logging

logger = app_logging.get_app_logger(__name__)

class DailyWindow(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)
        top_panel = wx.Panel(parent)
        
        top_sizer = wx.BoxSizer(wx.VERTICAL)

        top_section = wx.BoxSizer(wx.HORIZONTAL)
        calendar_static_box = wx.StaticBox(top_panel, -1, "date")
        calendar_box_sizer = wx.StaticBoxSizer(calendar_static_box, wx.VERTICAL)

        self.calendar_ctrl = wx.adv.CalendarCtrl(top_panel, wx.ID_ANY, wx.DateTime.Now(), wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS)
        calendar_box_sizer.Add(self.calendar_ctrl, 0, wx.ALL, 10)

        activity_weight_static_box = wx.StaticBox(top_panel, -1, "Activity/Weight")
        activity_weight_box_sizer = wx.StaticBoxSizer(activity_weight_static_box, wx.VERTICAL)

        activity_box_sizer = wx.BoxSizer(wx.VERTICAL)
        activity_row_sizer = wx.BoxSizer(wx.HORIZONTAL)
        add_activity_static_text = wx.StaticText(top_panel, -1, "Activity", wx.DefaultPosition, wx.Size(100, 20), wx.ALIGN_LEFT)
        self.add_activity_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        self.add_activity_button = wx.Button(top_panel, -1, "Add")
        activity_row_sizer.Add(add_activity_static_text, 0, wx.ALL, 10)
        activity_row_sizer.Add(self.add_activity_text_ctrl, 0, wx.ALL, 10)
        activity_row_sizer.Add(self.add_activity_button, 0, wx.ALL, 10)
        activity_box_sizer.Add(activity_row_sizer, 0, wx.ALL, 10)

        weight_row_sizer = wx.BoxSizer(wx.HORIZONTAL)
        add_weight_static_text = wx.StaticText(top_panel, -1, "Weight", wx.DefaultPosition, wx.Size(100, 20), wx.ALIGN_LEFT)
        self.add_weight_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        self.add_weight_button = wx.Button(top_panel, -1, "Add")
        weight_row_sizer.Add(add_weight_static_text, 0, wx.ALL, 10)
        weight_row_sizer.Add(self.add_weight_text_ctrl, 0, wx.ALL, 10)
        weight_row_sizer.Add(self.add_weight_button, 0, wx.ALL, 10)
        activity_box_sizer.Add(weight_row_sizer, 0, wx.ALL, 10)

        activity_weight_box_sizer.Add(activity_box_sizer, 0, wx.ALL, 10)

        add_food_sizer = wx.BoxSizer(wx.HORIZONTAL)
        add_food_sizer.Add(wx.StaticText(top_panel, -1, "Multiplier", wx.DefaultPosition, wx.Size(100, 20), wx.ALIGN_LEFT), 0, wx.ALL, 10)
        self.unit_combo_box = wx.ComboBox(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        add_food_sizer.Add(self.unit_combo_box, 0, wx.ALL, 10)
        self.add_food_button = wx.Button(top_panel, -1, "Add Food")
        add_food_sizer.Add(self.add_food_button, 0, wx.ALL, 10)
        self.add_recipe_button = wx.Button(top_panel, -1, "Add Recipe")
        add_food_sizer.Add(self.add_recipe_button, 0, wx.ALL, 10)
        self.add_one_off_button = wx.Button(top_panel, -1, "Add One-Off")
        add_food_sizer.Add(self.add_one_off_button, 0, wx.ALL, 10)
        
        top_section.Add(activity_weight_box_sizer, 0, wx.ALL, 10)
        top_section.Add(calendar_box_sizer, 0, wx.ALL, 10)

        self.food_list_view = wx.ListView(top_panel, -1, style=wx.LC_REPORT)
        self.food_list_view.InsertColumn(0, 'ID', width=100)
        self.food_list_view.InsertColumn(1, 'Food/Recipe Name', width=320)
        self.food_list_view.InsertColumn(2, 'Calories', width=100)
        self.food_list_view.InsertColumn(3, 'Fat g', width=100)
        self.food_list_view.InsertColumn(4, 'Protein g', width=100)
        self.food_list_view.InsertColumn(5, 'Carbs g', width=100)

        macro_sizer = wx.BoxSizer(wx.HORIZONTAL)
        macro_sizer.Add(wx.StaticText(top_panel, -1, "Fat Percent: ", wx.DefaultPosition, wx.Size(100, 20), wx.ALIGN_LEFT), 0, wx.ALL, 10)
        self.percent_fat_text_ctrl = wx.TextCtrl(top_panel, -1, "1", wx.DefaultPosition, wx.Size(40, 20))
        macro_sizer.Add(self.percent_fat_text_ctrl, 0, wx.ALL, 10)
        macro_sizer.Add(wx.StaticText(top_panel, -1, "Protein Percent: ", wx.DefaultPosition, wx.Size(100, 20), wx.ALIGN_LEFT), 0, wx.ALL, 10)
        self.percent_protein_text_ctrl = wx.TextCtrl(top_panel, -1, "todo", wx.DefaultPosition, wx.Size(40, 20))
        macro_sizer.Add(self.percent_protein_text_ctrl, 0, wx.ALL, 10)
        macro_sizer.Add(wx.StaticText(top_panel, -1, "Carbs Percent: ", wx.DefaultPosition, wx.Size(100, 20), wx.ALIGN_LEFT), 0, wx.ALL, 10)
        self.percent_carbs_text_ctrl = wx.TextCtrl(top_panel, -1, "todo", wx.DefaultPosition, wx.Size(40, 20))
        macro_sizer.Add(self.percent_carbs_text_ctrl, 0, wx.ALL, 10)

        top_sizer.Add(top_section, 0, wx.EXPAND)
        top_sizer.Add(add_food_sizer, 0, wx.ALL, 5)
        top_sizer.Add(self.food_list_view, 2, wx.EXPAND)
        top_sizer.Add(macro_sizer, 0, wx.ALL, 10)

        top_panel.SetSizer(top_sizer)
        parent.AddPage(top_panel, "Daily")

    def reset_daily_multiplier(self, increments, default_index):
        self.unit_combo_box.Clear()
        for i in increments:
            self.unit_combo_box.Append(i)
        self.unit_combo_box.SetSelection(default_index)

    def set_daily_foods(self, food_list):
        self.food_list_view.DeleteAllItems()
        for food in food_list:
            self.food_list_view.InsertItem(0, str(food.xref_id))
            self.food_list_view.SetItem(0, 1, food.name)
            self.food_list_view.SetItem(0, 2, str(food.calories))
            self.food_list_view.SetItem(0, 3, str(food.fat))
            self.food_list_view.SetItem(0, 4, str(food.protein))
            self.food_list_view.SetItem(0, 5, str(food.carbs))
