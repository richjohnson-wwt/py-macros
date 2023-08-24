
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
    def __init__(self):
        self.conn = sqlite3.connect('my-macro.sqlite3')
        self.cursor = self.conn.cursor()
        self.selected_food = None
        self.subscribers = []

    def register(self, subscriber):
        logger.debug("Registering subscriber: " + str(subscriber))
        self.subscribers.append(subscriber)

    def notify(self):
        logger.debug("Subscriber size: " + str(len(self.subscribers)))
        for subscriber in self.subscribers:
            logger.debug("Notifying subscriber: " + str(subscriber))
            subscriber.on_food_change(self.selected_food)

    def get_foods(self):
        logger.info("Getting foods")
        foods = []
        for row in self.cursor.execute('SELECT * FROM Foods'):
            foods.append(Food(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        return foods

    def set_selected_food(self, food_id):
        logger.debug("Setting selected food: " + str(food_id))
        self.selected_food = food_id
        self.notify()

    def get_food(self, food_id):
        logger.debug("Getting food: " + str(food_id))
        for row in self.cursor.execute('SELECT * FROM Foods WHERE food_id = ?', (food_id,)):
            return Food(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        

