
import wx

from layout_helper import create_label_with_text_sizer

class OneOffDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, "One-Off", size=(400, 300))
        
        box_sizer = wx.BoxSizer(wx.VERTICAL)

        self.name_text_ctrl = wx.TextCtrl(self, -1, "", size=(200, -1))
        box_sizer.Add(create_label_with_text_sizer(self, "Name: ", self.name_text_ctrl), 0, wx.ALL, 10)

        self.food_fat_text_ctrl = wx.TextCtrl(self, -1, "", size=(200, -1))
        box_sizer.Add(create_label_with_text_sizer(self, "Fat: ", self.food_fat_text_ctrl), 0, wx.ALL, 10)

        self.food_protein_text_ctrl = wx.TextCtrl(self, -1, "", size=(200, -1))
        box_sizer.Add(create_label_with_text_sizer(self, "Protein: ", self.food_protein_text_ctrl), 0, wx.ALL, 10)

        self.food_carbs_text_ctrl = wx.TextCtrl(self, -1, "", size=(200, -1))
        box_sizer.Add(create_label_with_text_sizer(self, "Carbs: ", self.food_carbs_text_ctrl), 0, wx.ALL, 10)

        self.food_calories_text_ctrl = wx.TextCtrl(self, -1, "", size=(200, -1))
        box_sizer.Add(create_label_with_text_sizer(self, "Calories: ", self.food_calories_text_ctrl), 0, wx.ALL, 10)

        main_box_sizer = wx.BoxSizer(wx.VERTICAL)
        main_box_sizer.Add(box_sizer, 0, wx.ALL, 10)
        # add ok and cancel buttons
        self.ok_button = wx.Button(self, wx.ID_OK, "OK")
        self.cancel_button = wx.Button(self, wx.ID_CANCEL, "Cancel")
        main_box_sizer.Add(self.ok_button, 0, wx.ALL, 10)
        main_box_sizer.Add(self.cancel_button, 0, wx.ALL, 10)

        self.SetSizer(main_box_sizer)
        self.Fit()

    def get_name(self):
        return self.name_text_ctrl.GetValue()

    def get_fat(self):
        return self.food_fat_text_ctrl.GetValue()

    def get_protein(self):
        return self.food_protein_text_ctrl.GetValue()

    def get_carbs(self):
        return self.food_carbs_text_ctrl.GetValue()

    def get_calories(self):
        return self.food_calories_text_ctrl.GetValue()