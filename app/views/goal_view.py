
import wx
from layout_helper import create_label_with_text_sizer

class GoalWindow(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)
        top_panel = wx.Panel(parent)
        top_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.start_date_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(top_panel, "Start Date", self.start_date_text_ctrl), 0, wx.ALL, 10)

        self.target_weight_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(top_panel, "Target Weight", self.target_weight_text_ctrl), 0, wx.ALL, 10)

        self.bmr_calories_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(top_panel, "BMR Calories", self.bmr_calories_text_ctrl), 0, wx.ALL, 10)

        self.fat_percent_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(top_panel, "Fat Percent", self.fat_percent_text_ctrl), 0, wx.ALL, 10)

        self.protein_percent_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(top_panel, "Protein Percent", self.protein_percent_text_ctrl), 0, wx.ALL, 10)

        self.carbs_percent_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(top_panel, "Carbs Percent", self.carbs_percent_text_ctrl), 0, wx.ALL, 10)
        
        top_panel.SetSizer(top_sizer)
        parent.AddPage(top_panel, "Goal")

    def set_goal(self, goal):
        self.start_date_text_ctrl.SetValue(str(goal.start_date))
        self.target_weight_text_ctrl.SetValue(str(goal.target_weight))
        self.bmr_calories_text_ctrl.SetValue(str(goal.bmr_calories))
        self.fat_percent_text_ctrl.SetValue(str(goal.fat_percent))
        self.protein_percent_text_ctrl.SetValue(str(goal.protein_percent))
        self.carbs_percent_text_ctrl.SetValue(str(goal.carbs_percent))
