
import sqlite3

from app import app_logging
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
    def __init__(self):
        self.conn = sqlite3.connect('my-macro.sqlite3')
        self.cursor = self.conn.cursor()
        self.selected_recipe = None
        self.subscribers = []

    def register(self, subscriber):
        logger.debug("Registering subscriber: " + str(subscriber))
        self.subscribers.append(subscriber)

    def notify(self):
        logger.debug("Subscriber size: " + str(len(self.subscribers)))
        for subscriber in self.subscribers:
            logger.debug("Notifying subscriber: " + str(subscriber))
            subscriber.on_recipe_change(self.selected_recipe)

    def get_recipes(self):
        recipes = []
        for row in self.cursor.execute('SELECT * FROM Recipes'):
            recipes.append(Recipe(row[0], row[1], row[2], row[3], row[4], row[5]))
        return recipes

    def set_selected_recipe(self, recipe_id):
        logger.debug("Setting selected recipe: " + str(recipe_id))
        self.selected_recipe = recipe_id
        self.notify()

    def get_recipe(self, recipe_id):
        logger.debug("Getting recipe: " + str(recipe_id))
        for row in self.cursor.execute('SELECT * FROM Recipes WHERE recipe_id = ?', (recipe_id,)):
            return Recipe(row[0], row[1], row[2], row[3], row[4], row[5])

    def get_food(self, food_id):
        logger.debug("Getting food: " + str(food_id))
        for row in self.cursor.execute('SELECT * FROM Foods WHERE food_id = ?', (food_id,)):
            return Food(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

    def get_unit(self, unit_id):
        logger.debug("Getting unit: " + str(unit_id))
        for row in self.cursor.execute('SELECT * FROM Units WHERE unit_id = ?', (unit_id,)):
            return Unit(row[0], row[1])

    def get_ingredients(self, recipe_id):
        logger.debug("Getting ingredients: " + str(recipe_id))
        ingredients = []
        for row in self.cursor.execute('SELECT * FROM xref_recipe_foods WHERE recipe_id = ?', (recipe_id,)).fetchall():
            i = Ingredient(self.get_food(row[1]), row[2], self.get_unit(row[3]))
            ingredients.append(i)
        logger.debug("ingredients size: " + str(len(ingredients)))
        return ingredients
