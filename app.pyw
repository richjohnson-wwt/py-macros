
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

import daily_model
import daily_view


import food_model
import food_view

import recipe_model
import recipe_view

import goal_model
import goal_view


import wx
import wx.lib.agw.aui as aui

aui_mgr = MyAuiManager()

# create all of the MVPs
single_food_model = food_model.FoodModel()
single_recipe_model = recipe_model.RecipeModel()
explorer_window = explorer_view.ExplorerWindow(aui_mgr)
food_list_presenter = explorer_presenter.FoodListPresenter(
    single_food_model,
    explorer_view.FoodListView(explorer_window.notebook_ctrl()),
    explorer_interactor.FoodListInteractor())

recipe_list_presenter = explorer_presenter.RecipeListPresenter(
    single_recipe_model,
    explorer_view.RecipeListView(explorer_window.notebook_ctrl()),
    explorer_interactor.RecipeListInteractor())

explorer_presenter.ExplorerPresenter(
    food_list_presenter, recipe_list_presenter
)
explorer_window.post_init()

main_window = main_view.MainWindow(aui_mgr)
daily = main_presenter.DailyPresenter(
    daily_model.DailyModel(),
    daily_view.DailyWindow(main_window.notebook_ctrl()),
    main_interactor.DailyInteractor())

food = main_presenter.FoodPresenter(
    single_food_model,
    food_view.FoodWindow(main_window.notebook_ctrl()),
    main_interactor.FoodInteractor())

recipe = main_presenter.RecipePresenter(
    single_recipe_model,
    recipe_view.RecipeWindow(main_window.notebook_ctrl()),
    main_interactor.RecipeInteractor())

goal = main_presenter.GoalPresenter(
    goal_model.GoalModel(),
    goal_view.GoalWindow(main_window.notebook_ctrl()),
    main_interactor.GoalInteractor())

main_presenter.MainPresenter(
    daily, food, recipe, goal
)
main_window.post_init()

aui_mgr.start()

