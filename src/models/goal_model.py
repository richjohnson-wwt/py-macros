
import sqlite3

from src import app_logging

logger = app_logging.get_app_logger(__name__)

class Goal:
    def __init__(self, id, start_date, target_weight, bmr_calories, fat_percent, protein_percent, carbs_percent):
        self.id = id
        self.start_date = start_date
        self.target_weight = target_weight
        self.bmr_calories = bmr_calories
        self.fat_percent = fat_percent
        self.protein_percent = protein_percent
        self.carbs_percent = carbs_percent


class GoalModel(object):
    def __init__(self):
        self.conn = sqlite3.connect('my-macro.sqlite3')
        self.cursor = self.conn.cursor()

    def get_goal(self):
        logger.debug("Getting goal")
        goals = []
        for row in self.cursor.execute('SELECT * FROM goal'):
            goals.append(Goal(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return goals[0]