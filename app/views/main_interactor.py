

import wx

class MainInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view


class DailyInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view


class FoodInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view


class RecipeInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view


class GoalInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view