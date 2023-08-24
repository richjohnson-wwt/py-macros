
import wx

class GoalWindow(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)
        tabGoal = wx.Panel(parent)
        foobar_sizer = wx.BoxSizer(wx.VERTICAL)
        foo1 = wx.StaticText(tabGoal, -1, "Goal Tab1")
        foobar_sizer.Add(foo1, 0, wx.EXPAND)
        foo2 = wx.StaticText(tabGoal, -1, "Goal Tab2")
        foobar_sizer.Add(foo2, 0, wx.EXPAND)
        foo3 = wx.StaticText(tabGoal, -1, "Goal Tab3")
        foobar_sizer.Add(foo3, 0, wx.EXPAND)
        foo4 = wx.StaticText(tabGoal, -1, "Goal Tab4")
        foobar_sizer.Add(foo4, 0, wx.EXPAND)
        foo5 = wx.StaticText(tabGoal, -1, "Goal Tab5")
        foobar_sizer.Add(foo5, 0, wx.EXPAND)
        tabGoal.SetSizer(foobar_sizer)
        parent.AddPage(tabGoal, "Goal")
