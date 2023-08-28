
import wx
import wx.aui

class MyAuiManager(wx.Frame):
    def __init__(self, parent):
        # self.app = wx.App(0)
        wx.Frame.__init__(self, parent, -1, "Py In/Out", size=(1400, 900))

        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(parent)

    # def install_left(self, view, title=""):
    #     self.explorer_pane = view
    #     self._mgr.AddPane(self.explorer_pane, wx.LEFT, title)

    def install_center(self, view, title=""):
        self._mgr.AddPane(view, wx.CENTER, title)

    def install_bottom(self, view, title=""):
        self.progress_pane = view
        self._mgr.AddPane(self.progress_pane, wx.BOTTOM, title)
        

    def start(self):

        # self._mgr.GetPane(self.explorer_pane).MinSize(450, -1)
        # self._mgr.GetPane(self.leftPane).Fixed()

        # self._mgr.GetPane(self.progress_pane).MinSize(-1, 200)

        self._mgr.Update()
        self.Show()
        # self.app.MainLoop()