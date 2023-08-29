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
        _main_model = main_model.MainModel()
        _unit_model = unit_model.UnitModel()
        _food_model = food_model.FoodModel(['list_changed', 'item_selected'])
        _recipe_model = recipe_model.RecipeModel(['list_changed', 'item_selected'])
        _explorer_model = explorer_model.ExplorerModel(_food_model, _recipe_model)

        self.explorer_window = explorer_view.ExplorerWindow(parent)
        self.food_list_presenter = explorer_presenter.FoodListPresenter(
            _food_model,
            self.explorer_window.food_page,
            explorer_interactor.FoodListInteractor(),
            _explorer_model
        )

        self.recipe_list_presenter = explorer_presenter.RecipeListPresenter(
            _recipe_model,
            self.explorer_window.recipe_page,
            explorer_interactor.RecipeListInteractor(),
            _explorer_model
        )
        
        _daily_model = daily_model.DailyModel()
        _goal_model = goal_model.GoalModel()
        # _daily_view = daily_view.DailyWindow(parent)
        # _food_view = food_view.FoodWindow(parent)
        # _recipe_view = recipe_view.RecipeWindow(parent)
        # _goal_view = goal_view.GoalWindow(parent)
        self.main_window = main_view.MainWindow(parent)
        _main_presenter = main_presenter.MainPresenter(
            _main_model,
            self.main_window,
            main_interactor.MainInteractor()
        )
        
        self.daily_presenter = main_presenter.DailyPresenter(
            _daily_model,
            self.main_window.daily_page,
            main_interactor.DailyInteractor(),
            _food_model,
            _recipe_model,
            _goal_model,
            macro_calculator.MacroCalculator()
        )
        
        self.food_presenter = main_presenter.FoodPresenter(
            _food_model,
            self.main_window.food_page,
            main_interactor.FoodInteractor(),
            _unit_model,
            _main_model
        )
        
        self.recipe_presenter = main_presenter.RecipePresenter(
            _recipe_model,
            self.main_window.recipe_page,
            main_interactor.RecipeInteractor(),
            _unit_model,
            _main_model,
            _food_model
        )
        
        self.goal_presenter = main_presenter.GoalPresenter(
            _goal_model,
            self.main_window.goal_page,
            main_interactor.GoalInteractor()
        )

        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(parent)


    def create(self):
        logging.info("Creating app")
        self._mgr.AddPane(self.explorer_window, wx.LEFT, "Explorer")

        self._mgr.AddPane(self.main_window, wx.CENTER, "Main")


        text2 = wx.TextCtrl(self.wx_frame, -1, 'Pane 3 - sample text',
                            wx.DefaultPosition, wx.Size(200,150),
                            wx.NO_BORDER | wx.TE_MULTILINE)
        self._mgr.AddPane(text2, wx.BOTTOM, "Pane 3")

        self._mgr.Update()
        

    def start(self):
        self.food_list_presenter.post_init()
        self.recipe_list_presenter.post_init()
        self.daily_presenter.post_init()
        self.food_presenter.post_init()
        self.recipe_presenter.post_init()
        self.goal_presenter.post_init()
