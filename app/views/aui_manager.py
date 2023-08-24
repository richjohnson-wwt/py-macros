
import wx
import wx.lib.agw.aui as aui

class MyAuiManager(wx.Frame):
    def __init__(self):
        self.app = wx.App(0)
        wx.Frame.__init__(self, None, -1, "AUI Manager", size=(1400, 900))

        self._mgr = aui.AuiManager(self)

    def InstallLeft(self, view, title=""):
        self.leftPane = view
        self._mgr.AddPane(view, wx.LEFT, title)

    def InstallCenter(self, view, title=""):
        self._mgr.AddPane(view, wx.CENTER, title)

    def InstallBottom(self, view, title=""):
        self._mgr.AddPane(view, wx.BOTTOM, title)
        

    def start(self):

        self._mgr.GetPane(self.leftPane).MinSize(400, -1)
        # self._mgr.GetPane(self.leftPane).Fixed()
        self._mgr.Update()
        self.Show()
        self.app.MainLoop()