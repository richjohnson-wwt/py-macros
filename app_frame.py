
import wx
import macro_app

class AppFrame(wx.Frame):
    def __init__(self):
        self.app = wx.App(0)
        wx.Frame.__init__(self, None, -1, "Macro App", size=(1400, 900))
        self.macro_app = macro_app.MacroApp(self)
        self.macro_app.create()

    def post_init(self):
        self.macro_app.start()
        self.Show()
        self.app.MainLoop()
