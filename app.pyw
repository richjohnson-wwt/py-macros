
import logging
import sys
sys.path.append('app/views')
sys.path.append('app/presenters')
sys.path.append('app/models')

# from aui_manager import MyAuiManager
# import explorer_presenter
# import explorer_model
# import explorer_view
# import explorer_interactor

# import main_interactor
# import main_view
# import main_presenter
# import main_model

# import progress_presenter
# import progress_view

# import daily_model
# import daily_view
# import macro_calculator


# import food_model
# import food_view

# import recipe_model
# import recipe_view

# import goal_model
# import goal_view

# import unit_model

import app_frame
import wx


_app_frame = app_frame.AppFrame()
_app_frame.post_init()

# create all of the MVPs
"""
_single_main_model = main_model.MainModel()
_single_unit_model = unit_model.UnitModel()

_single_food_model = food_model.FoodModel(['list_changed', 'item_selected'])
_single_recipe_model = recipe_model.RecipeModel(['list_changed', 'item_selected'])
_single_explorer_model = explorer_model.ExplorerModel(_single_food_model, _single_recipe_model)
_explorer_window = explorer_view.ExplorerWindow(_aui_mgr)
_food_list_presenter = explorer_presenter.FoodListPresenter(
    _single_food_model,
    explorer_view.FoodListView(_explorer_window.notebook_ctrl()),
    explorer_interactor.FoodListInteractor(),
    _single_explorer_model
)

_recipe_list_presenter = explorer_presenter.RecipeListPresenter(
    _single_recipe_model,
    explorer_view.RecipeListView(_explorer_window.notebook_ctrl()),
    explorer_interactor.RecipeListInteractor(),
    _single_explorer_model
)

_explorer_window.post_init()
_food_list_presenter.post_init()
_recipe_list_presenter.post_init()

_main_window = main_view.MainWindow(_aui_mgr)
_daily_model = daily_model.DailyModel()
_goal_model = goal_model.GoalModel()
_main_presenter = main_presenter.MainPresenter(
    _single_main_model,
    _main_window,
    main_interactor.MainInteractor()
)

_daily_presenter = main_presenter.DailyPresenter(
    _daily_model,
    daily_view.DailyWindow(_main_window.notebook_ctrl()),
    main_interactor.DailyInteractor(),
    _single_food_model,
    _single_recipe_model,
    _goal_model,
    macro_calculator.MacroCalculator()
)

_food_presenter = main_presenter.FoodPresenter(
    _single_food_model,
    food_view.FoodWindow(_main_window.notebook_ctrl()),
    main_interactor.FoodInteractor(),
    _single_unit_model,
    _single_main_model
)

_recipe_presenter = main_presenter.RecipePresenter(
    _single_recipe_model,
    recipe_view.RecipeWindow(_main_window.notebook_ctrl()),
    main_interactor.RecipeInteractor(),
    _single_unit_model,
    _single_main_model,
    _single_food_model
)

_goal_presenter = main_presenter.GoalPresenter(
    _goal_model,
    goal_view.GoalWindow(_main_window.notebook_ctrl()),
    main_interactor.GoalInteractor()
)


_main_window.post_init()
_daily_presenter.post_init()
_food_presenter.post_init()
_recipe_presenter.post_init()
_goal_presenter.post_init()

_progress_presenter = progress_presenter.ProgressPresenter(
    _daily_model, _goal_model, progress_view.ProgressWindow(_aui_mgr)
)

_aui_mgr = MyAuiManager()

_progress_presenter.post_init()

_aui_mgr.start()
"""

