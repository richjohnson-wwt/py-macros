
import wx

class MainNotebook(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.InitUI()

    def InitUI(self):
        self.main_panel = wx.Panel(self)

        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.notebook = wx.Notebook(self.main_panel)

        tabDaily = wx.Panel(self.notebook)

        tabFood = wx.Panel(self.notebook)

        tabRecipes = wx.Panel(self.notebook)

        tabGoal = wx.Panel(self.notebook)

        t1_text = wx.StaticText(tabDaily, -1, label="daily")
        t1sizer = wx.BoxSizer(wx.VERTICAL)
        t1sizer.Add(t1_text, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        tabDaily.SetSizer(t1sizer)
        self.notebook.AddPage(tabDaily, "Daily")

        t2_text = wx.StaticText(tabFood, -1, label="food")
        t2sizer = wx.BoxSizer(wx.VERTICAL)
        t2sizer.Add(t2_text, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        tabFood.SetSizer(t2sizer)
        self.notebook.AddPage(tabFood, "Food")

        t3_text = wx.StaticText(tabRecipes, -1, label="recipes")
        t3sizer = wx.BoxSizer(wx.VERTICAL)
        t3sizer.Add(t3_text, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        tabRecipes.SetSizer(t3sizer)
        self.notebook.AddPage(tabRecipes, "Recipes")

        t4_text = wx.StaticText(tabGoal, -1, label="goal")
        t4sizer = wx.BoxSizer(wx.VERTICAL)
        t4sizer.Add(t4_text, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        tabGoal.SetSizer(t4sizer)
        self.notebook.AddPage(tabGoal, "Goal")

        self.mainsizer.Add(self.notebook, 1, wx.EXPAND)
        self.main_panel.SetSizerAndFit(self.mainsizer)

        self.Centre()
        self.Show(True)
