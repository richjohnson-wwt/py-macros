
import wx


class FoodListInteractor:
    def install(self, presenter, view):
        self.presenter = presenter
        self.view = view
        self.view.food_list_view.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_food_item_selected)
        self.view.food_list_view.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
        self.view.search_text_ctrl.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.on_search)
        self.view.search_text_ctrl.Bind(wx.EVT_SEARCHCTRL_CANCEL_BTN, self.on_cancel)

    def on_food_item_selected(self, event):
        list_item = event.GetItem()
        self.presenter.on_food_item_selected(list_item.GetText())

    def on_key_down(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            self.presenter.on_delete_food()

    def on_search(self, event):
        search_string = event.GetString()
        self.presenter.on_search(search_string)

    def on_cancel(self, event):
        self.presenter.on_cancel()

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
