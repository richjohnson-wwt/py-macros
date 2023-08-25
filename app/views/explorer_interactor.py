
import wx


class FoodListInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view
        self.view.food_list_view.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_food_item_selected)
        self.view.food_list_view.Bind(wx.EVT_KEY_DOWN, self.on_key_down)

    def on_food_item_selected(self, event):
        list_item = event.GetItem()
        self.presenter.on_food_item_selected(list_item.GetText())

    def on_key_down(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            self.presenter.on_delete_food()

class RecipeListInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view
        self.view.recipe_list_view.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_recipe_item_selected)
        self.view.recipe_list_view.Bind(wx.EVT_KEY_DOWN, self.on_key_down)

    def on_recipe_item_selected(self, event):
        list_item = event.GetItem()
        self.presenter.on_recipe_item_selected(list_item.GetText())

    def on_key_down(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            self.presenter.on_delete_recipe()
