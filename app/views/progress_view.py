
import wx

from layout_helper import create_label_with_text_sizer

class ProgressWindow(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        top_panel = wx.Panel(self)
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)

        left_static_box = wx.StaticBox(top_panel, -1, "&Last 7 Days")
        left_static_box_sizer = wx.StaticBoxSizer(left_static_box, wx.VERTICAL)

        sizer_first_row = wx.BoxSizer(wx.HORIZONTAL)
        self.bmr_plus_exercise_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(100, 20))
        sizer_first_row.Add(create_label_with_text_sizer(top_panel, "BMR + Exercise: ", self.bmr_plus_exercise_text_ctrl, ), 0, wx.ALL, 10)
        self.consumed_calories_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(100, 20))
        sizer_first_row.Add(create_label_with_text_sizer(top_panel, " - Consumed Calories: ", self.consumed_calories_text_ctrl, ), 0, wx.ALL, 10)
        left_static_box_sizer.Add(sizer_first_row, 0, wx.ALL)

        sizer_second_row = wx.BoxSizer(wx.HORIZONTAL)
        self.net_in_out_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(100, 20))
        sizer_second_row.Add(create_label_with_text_sizer(top_panel, " = Net In/Out: ", self.net_in_out_text_ctrl, ), 0, wx.ALL, 10)
        self.activity_calories_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(100, 20))
        sizer_second_row.Add(create_label_with_text_sizer(top_panel, "Activity Calories: ", self.activity_calories_text_ctrl, ), 0, wx.ALL, 10)
        left_static_box_sizer.Add(sizer_second_row, 0, wx.ALL)

        self.expected_weight_delta_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(100, 20))
        left_static_box_sizer.Add(create_label_with_text_sizer(top_panel, "Expected Weight +/-: ", self.expected_weight_delta_text_ctrl, ), 0, wx.ALL, 10)

        # weight box
        right_static_box = wx.StaticBox(top_panel, -1, "&Weight")
        right_static_box_sizer = wx.StaticBoxSizer(right_static_box, wx.VERTICAL)
        self.progress_date_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(100, 20))
        right_static_box_sizer.Add(create_label_with_text_sizer(top_panel, "Progress Date: ", self.progress_date_text_ctrl, ), 0, wx.ALL, 10)
        self.goal_date_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(100, 20))
        right_static_box_sizer.Add(create_label_with_text_sizer(top_panel, "Goal Date: ", self.goal_date_text_ctrl, ), 0, wx.ALL, 10)
        self.actual_weight_diff_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(100, 20))
        right_static_box_sizer.Add(create_label_with_text_sizer(top_panel, "Actual Weight +/-: ", self.actual_weight_diff_text_ctrl, ), 0, wx.ALL, 10)

        top_sizer.Add(left_static_box_sizer, 0, wx.GROW | wx.ALL, 10)
        top_sizer.Add(right_static_box_sizer, 0, wx.GROW | wx.ALL, 10)
        top_panel.SetSizerAndFit(top_sizer)
