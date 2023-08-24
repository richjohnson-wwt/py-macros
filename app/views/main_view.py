
import wx

from app import app_logging

logger = app_logging.get_app_logger(__name__)

class MainWindow(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.main_panel = wx.Panel(self)
        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.notebook = wx.Notebook(self.main_panel, style=wx.BK_DEFAULT, size=(800, 600))
        parent.InstallCenter(self, "Main")

    def notebook_ctrl(self):
        return self.notebook

    def post_init(self):
        logger.info("Post init")
        self.mainsizer.Add(self.notebook, 5, wx.ALL, 10)
        self.main_panel.SetSizerAndFit(self.mainsizer)
        self.Centre()
