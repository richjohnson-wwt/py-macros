
import wx

def create_label_with_text_sizer(panel, label_text, text_ctrl):
    sizer = wx.BoxSizer(wx.HORIZONTAL)
    sizer.Add(wx.StaticText(panel, -1, label_text, wx.DefaultPosition, wx.Size(150, 20), wx.ALIGN_LEFT))
    sizer.Add(text_ctrl, wx.ALIGN_LEFT)
    return sizer
