import logging
import sys
sys.path.append('app/views')
sys.path.append('app/presenters')
sys.path.append('app/models')

from aui_manager import MyAuiManager
import explorer_presenter
import explorer_model
import explorer_view
import explorer_interactor

import main_interactor
import main_view
import main_presenter
import main_model

import progress_presenter
import progress_view

import daily_model
import daily_view
import macro_calculator


import food_model
import food_view

import recipe_model
import recipe_view

import goal_model
import goal_view

import unit_model

import wx

from app import app_logging

logger = app_logging.get_app_logger(__name__)

class MacroApp(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Macro App", size=(1400, 900))
        self.wx_frame = parent
        self.main_model = main_model.MainModel()
        self.unit_model = unit_model.UnitModel()
        self.food_model = food_model.FoodModel(['list_changed', 'item_selected'])
        self.recipe_model = recipe_model.RecipeModel(['list_changed', 'item_selected'])
        self.explorer_model = explorer_model.ExplorerModel(self.food_model, self.recipe_model)

        self.food_list_view = explorer_view.FoodListView()
        self.recipe_list_view = explorer_view.RecipeListView()
        self.explorer_window = explorer_view.ExplorerWindow(parent, self.food_list_view, self.recipe_list_view)
        self.food_list_presenter = explorer_presenter.FoodListPresenter(
            self.food_model,
            self.food_list_view,
            explorer_interactor.FoodListInteractor(),
            self.explorer_model
        )

        self.recipe_list_presenter = explorer_presenter.RecipeListPresenter(
            self.recipe_model,
            self.recipe_list_view,
            explorer_interactor.RecipeListInteractor(),
            self.explorer_model
        )

        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(parent)


    def create(self):
        logging.info("Creating app")
        notebook = self.explorer_window.create_explorer_notebook()

        self._mgr.AddPane(notebook, wx.LEFT, "Explorer")

        text1 = wx.TextCtrl(self.wx_frame, -1, 'Pane 2 - sample text',
                            wx.DefaultPosition, wx.Size(200,150),
                            wx.NO_BORDER | wx.TE_MULTILINE)
        self._mgr.AddPane(text1, wx.CENTER, "Pane 2")

        text2 = wx.TextCtrl(self.wx_frame, -1, 'Pane 3 - sample text',
                            wx.DefaultPosition, wx.Size(200,150),
                            wx.NO_BORDER | wx.TE_MULTILINE)
        self._mgr.AddPane(text2, wx.BOTTOM, "Pane 3")

        self._mgr.Update()

        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_close(self, event):
        logger.info("Closing app")
        self._mgr.UnInit()
        self.Destroy()

    # def post_init(self):
    #     logger.info("MacroApp Post init")
    #     self.Show()