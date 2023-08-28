
import wx

from app import app_logging

logger = app_logging.get_app_logger(__name__)

class MainWindow(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.main_panel = wx.Panel(self)
        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.notebook = wx.Notebook(self.main_panel)
        parent.install_center(self, "Main")

    def notebook_ctrl(self):
        return self.notebook

    def post_init(self):
        logger.info("Post init")
        self.mainsizer.Add(self.notebook, proportion=1, flag=wx.EXPAND | wx.ALL)
        self.main_panel.SetSizerAndFit(self.mainsizer)
        self.Centre()
