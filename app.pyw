
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

import progress_presenter
import progress_view

import daily_model
import daily_view

import food_model
import food_view

import recipe_model
import recipe_view

import goal_model
import goal_view

import unit_model

import wx
import wx.lib.agw.aui as aui

aui_mgr = MyAuiManager()

# create all of the MVPs
single_unit_model = unit_model.UnitModel()
single_food_model = food_model.FoodModel(['list_changed', 'item_selected'])
single_recipe_model = recipe_model.RecipeModel(['list_changed', 'item_selected'])
explorer_window = explorer_view.ExplorerWindow(aui_mgr)
food_list_presenter = explorer_presenter.FoodListPresenter(
    single_food_model,
    explorer_view.FoodListView(explorer_window.notebook_ctrl()),
    explorer_interactor.FoodListInteractor()
)

recipe_list_presenter = explorer_presenter.RecipeListPresenter(
    single_recipe_model,
    explorer_view.RecipeListView(explorer_window.notebook_ctrl()),
    explorer_interactor.RecipeListInteractor())

explorer_window.post_init()
food_list_presenter.post_init()
recipe_list_presenter.post_init()

main_window = main_view.MainWindow(aui_mgr)
daily_model = daily_model.DailyModel()
goal_model = goal_model.GoalModel()
daily = main_presenter.DailyPresenter(
    daily_model,
    daily_view.DailyWindow(main_window.notebook_ctrl()),
    main_interactor.DailyInteractor())

food = main_presenter.FoodPresenter(
    single_food_model,
    food_view.FoodWindow(main_window.notebook_ctrl()),
    main_interactor.FoodInteractor(),
    single_unit_model
)

recipe = main_presenter.RecipePresenter(
    single_recipe_model,
    recipe_view.RecipeWindow(main_window.notebook_ctrl()),
    main_interactor.RecipeInteractor())

goal = main_presenter.GoalPresenter(
    goal_model,
    goal_view.GoalWindow(main_window.notebook_ctrl()),
    main_interactor.GoalInteractor())


main_window.post_init()
daily.post_init()
food.post_init()
recipe.post_init()
goal.post_init()

progress_presenter = progress_presenter.ProgressPresenter(
    daily_model, goal_model, progress_view.ProgressWindow(aui_mgr)
)

progress_presenter.post_init()

aui_mgr.start()

