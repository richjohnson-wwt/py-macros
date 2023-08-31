
import wx
import wx.aui

class MyAuiManager(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Py In/Out", size=(1400, 900))
        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(parent)

    def start(self):
        self._mgr.Update()
        self.Show()
