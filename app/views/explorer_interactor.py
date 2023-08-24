
import wx


class FoodListInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view
        self.view.food_list_view.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_food_item_selected)

    def on_food_item_selected(self, event):
        list_item = event.GetItem()
        self.presenter.on_food_item_selected(list_item.GetText())

class RecipeListInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view
        self.view.recipe_list_view.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_recipe_item_selected)

    def on_recipe_item_selected(self, event):
        list_item = event.GetItem()
        self.presenter.on_recipe_item_selected(list_item.GetText())
