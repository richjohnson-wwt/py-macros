

import wx

class DailyWindow(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)
        tabDaily = wx.Panel(parent)
        foobar_sizer = wx.BoxSizer(wx.VERTICAL)
        foo1 = wx.StaticText(tabDaily, -1, "Daily Tab1")
        foobar_sizer.Add(foo1, 0, wx.EXPAND)
        foo2 = wx.StaticText(tabDaily, -1, "Daily Tab2")
        foobar_sizer.Add(foo2, 0, wx.EXPAND)
        foo3 = wx.StaticText(tabDaily, -1, "Daily Tab3")
        foobar_sizer.Add(foo3, 0, wx.EXPAND)
        foo4 = wx.StaticText(tabDaily, -1, "Daily Tab4")
        foobar_sizer.Add(foo4, 0, wx.EXPAND)
        foo5 = wx.StaticText(tabDaily, -1, "Daily Tab5")
        foobar_sizer.Add(foo5, 0, wx.EXPAND)
        food_list_view = wx.ListView(tabDaily, -1, style=wx.LC_REPORT)
        food_list_view.InsertColumn(0, 'ID', width=140)
        food_list_view.InsertColumn(1, 'Name', width=60)
        foobar_sizer.Add(food_list_view, 2, wx.EXPAND)
        tabDaily.SetSizer(foobar_sizer)
        parent.AddPage(tabDaily, "Daily")
        
