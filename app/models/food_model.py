
import sqlite3

from app import app_logging

logger = app_logging.get_app_logger(__name__)

# https://docs.python.org/3/library/sqlite3.html

class Food:
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
        self.selected_food = 1
        self.events = {event : dict() for event in events}

    def get_subscribers(self, event):
        return self.events[event]

    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback

    def notify(self, event, message=None):
        for subscriber, callback in self.get_subscribers(event).items():
            callback()

    def get_foods(self):
        logger.info("Getting foods")
        foods = []
        for row in self.cursor.execute('SELECT * FROM Foods'):
            foods.append(Food(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        return foods

    def set_selected_food(self, food_id):
        logger.debug("Setting selected food: " + str(food_id))
        self.selected_food = food_id
        self.notify('item_selected')

    def get_food(self):
        logger.debug("Getting food: " + str(self.selected_food))
        for row in self.cursor.execute('SELECT * FROM Foods WHERE food_id = ?', (self.selected_food,)):
            return Food(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        
    def create_new_food(self):
        logger.debug("Creating new food")
        new_name = "New Food"
        self.cursor.execute('INSERT INTO Foods (food_id, name, fat, protein, carb, calories, quantity, unit_id, popularity) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)', (new_name, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 0))
        self.conn.commit()
        # select last inserted row id
        self.cursor.execute('SELECT last_insert_rowid()')
        self.selected_food = self.cursor.fetchone()[0]
        logger.info("New food created: " + str(self.selected_food))
        self.notify('list_changed')

    def update_food(self, name, fat, protein, carb, calories, quantity, unit, popularity):
        logger.debug("Updating food")
        self.cursor.execute('UPDATE Foods SET name=?, fat=?, protein=?, carb=?, calories=?, quantity=?, unit_id=?, popularity=? WHERE food_id=?', (name, fat, protein, carb, calories, quantity, unit, popularity, self.selected_food))
        self.conn.commit()
        self.notify('list_changed')

    def delete_food(self):
        logger.debug("Deleting food: " + str(self.selected_food))
        self.cursor.execute('DELETE FROM Foods WHERE food_id = ?', (self.selected_food,))
        self.conn.commit()
        self.notify('list_changed')
