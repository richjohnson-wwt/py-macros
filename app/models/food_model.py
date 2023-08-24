
import sqlite3

from app import app_logging

logger = app_logging.get_app_logger(__name__)

# https://docs.python.org/3/library/sqlite3.html

class Food(object):
    def __init__(self, food_id, name, fat, protein, carbs, calories, quantity, unit_id, popularity):
        self.id = food_id
        self.name = name
        self.fat = fat
        self.protein = protein
        self.carbs = carbs
        self.calories = calories
        self.quantity = quantity
        self.unit_id = unit_id
        self.popularity = popularity

class FoodModel:
    def __init__(self, events):
        self.conn = sqlite3.connect('my-macro.sqlite3')
        self.cursor = self.conn.cursor()
        self.selected_food = None
        self.events = {event : dict() for event in events}

    def get_subscribers(self, event):
        return self.events[event]

    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback

    def notify(self, event, message=None):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)

    def get_foods(self):
        logger.info("Getting foods")
        foods = []
        for row in self.cursor.execute('SELECT * FROM Foods'):
            foods.append(Food(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        return foods

    def set_selected_food(self, food_id):
        logger.debug("Setting selected food: " + str(food_id))
        self.selected_food = food_id
        self.notify('item_selected', food_id)

    def get_food(self, food_id):
        logger.debug("Getting food: " + str(food_id))
        for row in self.cursor.execute('SELECT * FROM Foods WHERE food_id = ?', (food_id,)):
            return Food(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        

