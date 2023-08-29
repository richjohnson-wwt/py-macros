
import wx
from layout_helper import create_label_with_text_sizer

class GoalWindow(wx.Panel):
    def __init__(self, notebook):
        wx.Panel.__init__(self, notebook, id=wx.ID_ANY)
        # top_panel = wx.Panel(self)
        top_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.start_date_text_ctrl = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(self, "Start Date", self.start_date_text_ctrl), 0, wx.ALL, 10)

        self.target_weight_text_ctrl = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(self, "Target Weight", self.target_weight_text_ctrl), 0, wx.ALL, 10)

        self.bmr_calories_text_ctrl = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(self, "BMR Calories", self.bmr_calories_text_ctrl), 0, wx.ALL, 10)

        self.fat_percent_text_ctrl = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(self, "Fat Percent", self.fat_percent_text_ctrl), 0, wx.ALL, 10)

        self.protein_percent_text_ctrl = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(self, "Protein Percent", self.protein_percent_text_ctrl), 0, wx.ALL, 10)

        self.carbs_percent_text_ctrl = wx.TextCtrl(self, -1, "", wx.DefaultPosition, wx.Size(200, 20))
        top_sizer.Add(create_label_with_text_sizer(self, "Carbs Percent", self.carbs_percent_text_ctrl), 0, wx.ALL, 10)
        
        self.SetSizer(top_sizer)

    def set_goal(self, goal):
        self.start_date_text_ctrl.SetValue(str(goal.start_date))
        self.target_weight_text_ctrl.SetValue(str(goal.target_weight))
        self.bmr_calories_text_ctrl.SetValue(str(goal.bmr_calories))
        self.fat_percent_text_ctrl.SetValue(str(goal.fat_percent))
        self.protein_percent_text_ctrl.SetValue(str(goal.protein_percent))
        self.carbs_percent_text_ctrl.SetValue(str(goal.carbs_percent))
