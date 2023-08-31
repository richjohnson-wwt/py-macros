
import sqlite3

from src import app_logging
from food_model import Food
from unit_model import Unit

logger = app_logging.get_app_logger(__name__)

class Recipe:
    def __init__(self, recipe_id, name, instructions, description, url, servings):
        self.id = recipe_id
        self.name = name
        self.instructions = instructions
        self.description = description
        self.url = url
        self.servings = servings

class Ingredient:
    def __init__(self, food, unit_multiplier, unit):
        self.food = food
        self.unit_multiplier = unit_multiplier
        self.unit = unit

class RecipeModel:
    def __init__(self, events):
        self.conn = sqlite3.connect('my-macro.sqlite3')
        self.cursor = self.conn.cursor()
        self.selected_recipe = 3
        self.selected_ingredient = -1
        self.events = {event : dict() for event in events}

    def get_subscribers(self, event):
        return self.events[event]

    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback

    def notify(self, event):
        for subscriber, callback in self.get_subscribers(event).items():
            callback()

    def get_recipes(self):
        logger.debug("Getting recipes")
        recipes = []
        for row in self.cursor.execute('SELECT * FROM Recipes'):
            recipes.append(Recipe(row[0], row[1], row[2], row[3], row[4], row[5]))
        return recipes

    def set_selected_recipe(self, recipe_id):
        logger.debug("Setting selected recipe: " + str(recipe_id))
        self.selected_recipe = recipe_id
        self.notify('item_selected')

    def get_recipe(self):
        logger.debug("Getting recipe: " + str(self.selected_recipe))
        for row in self.cursor.execute('SELECT * FROM Recipes WHERE recipe_id = ?', (self.selected_recipe,)):
            return Recipe(row[0], row[1], row[2], row[3], row[4], row[5])

    def get_food(self, food_id):
        logger.debug("Getting food: " + str(food_id))
        for row in self.cursor.execute('SELECT * FROM Foods WHERE food_id = ?', (food_id,)):
            return Food(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

    def get_unit(self, unit_id):
        logger.debug("Getting unit: " + str(unit_id))
        for row in self.cursor.execute('SELECT * FROM Units WHERE unit_id = ?', (unit_id,)):
            return Unit(row[0], row[1])

    def get_ingredients(self):
        logger.debug("Getting ingredients: " + str(self.selected_recipe))
        ingredients = []
        for row in self.cursor.execute('SELECT * FROM xref_recipe_foods WHERE recipe_id = ?', (self.selected_recipe,)).fetchall():
            i = Ingredient(self.get_food(row[1]), row[2], self.get_unit(row[3]))
            ingredients.append(i)
        logger.debug("ingredients size: " + str(len(ingredients)))
        return ingredients

    def create_new_recipe(self):
        logger.debug("Creating new recipe")
        new_name = "New Recipe"
        self.cursor.execute('INSERT INTO Recipes (recipe_id, name, instructions, description, url, servings) VALUES (NULL, ?, ?, ?, ?, ?)', (new_name, '', '', '', 1))
        self.conn.commit()
        # select last inserted row id
        self.cursor.execute('SELECT last_insert_rowid()')
        self.selected_recipe = self.cursor.fetchone()[0]
        logger.debug("New recipe created: " + str(self.selected_recipe))
        self.notify('list_changed')

    def update_recipe(self, name, instructions, description, url, servings):
        logger.debug("Updating recipe")
        self.cursor.execute('UPDATE Recipes SET name = ?, instructions = ?, description = ?, url = ?, servings = ? WHERE recipe_id = ?', (name, instructions, description, url, servings, self.selected_recipe))
        self.conn.commit()
        self.notify('list_changed')

    def delete_ingredients(self):
        logger.debug("Deleting ingredients")
        self.cursor.execute('DELETE FROM xref_recipe_foods WHERE recipe_id = ?', (self.selected_recipe,))
        self.conn.commit()

    def add_recipe_ingredient(self, food_id, amount, unit_id):
        logger.debug("Adding ingredient")
        self.cursor.execute('INSERT INTO xref_recipe_foods (recipe_id, food_id,amount, unit_id) VALUES (?, ?, ?, ?)', (self.selected_recipe, food_id, amount, unit_id))
        self.conn.commit()

    def delete_recipe(self):
        logger.debug("Deleting recipe")
        # delete from recipes and xref_recipe_foods where recipe_id = ? in a transaction
        self.cursor.execute('DELETE FROM Recipes WHERE recipe_id = ?', (self.selected_recipe,))
        self.cursor.execute('DELETE FROM xref_recipe_foods WHERE recipe_id = ?', (self.selected_recipe,))
        self.conn.commit()
        self.notify('list_changed')

