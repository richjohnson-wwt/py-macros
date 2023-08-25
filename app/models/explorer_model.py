
class ExplorerModel:
    def __init__(self, food_model, recipe_model):
        self.food_model = food_model
        self.recipe_model = recipe_model


    def delete_food(self):
        self.food_model.delete_food()

    def delete_recipe(self):
        self.recipe_model.delete_recipe()