
import wx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

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
        sizer_second_row.Add(create_label_with_text_sizer(top_panel, " = Net Out: ", self.net_in_out_text_ctrl, ), 0, wx.ALL, 10)
        self.activity_calories_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(100, 20))
        sizer_second_row.Add(create_label_with_text_sizer(top_panel, "Activity Calories: ", self.activity_calories_text_ctrl, ), 0, wx.ALL, 10)
        left_static_box_sizer.Add(sizer_second_row, 0, wx.ALL)

        self.expected_weight_delta_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(100, 20))
        left_static_box_sizer.Add(create_label_with_text_sizer(top_panel, "Expected Weight +/-: ", self.expected_weight_delta_text_ctrl, ), 0, wx.ALL, 10)

        # weight box
        middle_static_box = wx.StaticBox(top_panel, -1, "&Weight")
        middle_static_box_sizer = wx.StaticBoxSizer(middle_static_box, wx.VERTICAL)
        self.progress_date_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(100, 20))
        middle_static_box_sizer.Add(create_label_with_text_sizer(top_panel, "Progress Date: ", self.progress_date_text_ctrl, ), 0, wx.ALL, 10)
        self.goal_date_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(100, 20))
        middle_static_box_sizer.Add(create_label_with_text_sizer(top_panel, "Goal Date: ", self.goal_date_text_ctrl, ), 0, wx.ALL, 10)
        self.actual_weight_diff_text_ctrl = wx.TextCtrl(top_panel, -1, "", wx.DefaultPosition, wx.Size(100, 20))
        middle_static_box_sizer.Add(create_label_with_text_sizer(top_panel, "Actual Weight +/-: ", self.actual_weight_diff_text_ctrl, ), 0, wx.ALL, 10)

        # macros box
        right_static_box = wx.StaticBox(top_panel, wx.ID_ANY, "&Today's Macros")
        right_static_box_sizer = wx.StaticBoxSizer(right_static_box, wx.VERTICAL)
        self.figure = plt.Figure()
        self.figure.set_facecolor('darkgray')
        self.figure.set_size_inches(2, 2)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_facecolor('darkgray')
        self.canvas = FigureCanvas(top_panel, wx.ID_ANY, self.figure)
        right_static_box_sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)

        top_sizer.Add(left_static_box_sizer, 0, wx.GROW | wx.ALL, 10)
        top_sizer.Add(middle_static_box_sizer, 0, wx.GROW | wx.ALL, 10)
        top_sizer.Add(right_static_box_sizer, 0, wx.GROW | wx.ALL, 10)

        top_panel.SetSizerAndFit(top_sizer)

    def draw_chart(self, labels, sizes):
        self.axes.clear()
        self.Fit()
        self.axes.plot(1, 0)

        self.axes.pie(sizes,
                         labels=labels,
                         autopct='%1.1f%%',
                         textprops={'size': 'smaller'},
                         shadow=True,
                         radius=0.5,
                         startangle=90)
        self.axes.axis('equal')
        
        self.figure.canvas.draw()
