
import wx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

class ChartWindow(wx.Panel):
    def __init__(self, notebook):
        wx.Panel.__init__(self, notebook, id=wx.ID_ANY)

        self.figure = plt.Figure()
        self.axes = self.figure.add_subplot(111)

    def draw_chart(self, x, y):
        x = np.array(x)
        y = np.array(y)
        x1 = x[:-1]
        y1 = y[:-1]

        a, b = np.polyfit(x1, y1, 1)

        self.axes.scatter(x, y)
        self.axes.plot(x, a * x + b)

        self.canvas = FigureCanvas(self, -1, self.figure)
        