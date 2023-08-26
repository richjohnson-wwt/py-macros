
import sqlite3

from app import app_logging

logger = app_logging.get_app_logger(__name__)

class XrefDailyFood:
    def __init__(self, xref_id, daily_food_id, name, fat, protein, carbs, calories):
        self.xref_id = xref_id
        self.daily_food_id = daily_food_id
        self.name = name
        self.fat = fat
        self.protein = protein
        self.carbs = carbs
        self.calories = calories
        

class DailyFood:
    def __init__(self, df_id, date, exercise, weight):
        self.daily_food_id = df_id
        self.date = date
        self.exercise = exercise
        self.weight = weight

class DailyModel:
    def __init__(self):
        self.conn = sqlite3.connect('my-macro.sqlite3')
        self.cursor = self.conn.cursor()
        # get today's date in sqlite3 format
        todays_date = self.cursor.execute('SELECT strftime("%Y-%m-%d", "now")').fetchone()
        self.selected_date = todays_date
        self.selected_xref_id = 0
        self.serving_increments = ["0.1", "0.25", "0.33", "0.5", "0.75", "1", "1.5", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        
    def set_selected_date(self, date):
        self.selected_date = date

    def set_selected_daily_food(self, xref_id):
        self.selected_xref_id = xref_id

    def get_today_date(self):
        for row in self.cursor.execute('SELECT strftime("%Y-%m-%d", "now")'):
            return row[0]

    def does_date_exist(self, today_date):
        logger.info("Does date exist: " + str(today_date))
        return self.cursor.execute('SELECT * FROM daily_food WHERE date = ?', (str(today_date),)).fetchone() is not None

    def create_daily_food(self, todays_date):
        logger.info("Creating daily food for today: " + str(todays_date))
        self.cursor.execute('INSERT INTO daily_food (date, exercise_calorie_bonus, weight) VALUES (?, ?, ?)', (str(todays_date), 0, 0))
        self.conn.commit()

    def update_exercise_calorie_bonus(self, exercise_calorie_bonus):
        logger.info("Updating exercise calorie bonus: " + str(exercise_calorie_bonus))
        self.cursor.execute('UPDATE daily_food SET exercise_calorie_bonus = ? WHERE date = ?', (str(exercise_calorie_bonus), str(self.selected_date)))
        self.conn.commit()

    def get_daily_food(self):
        logger.info("Getting daily food")
        for row in self.cursor.execute('SELECT * FROM daily_food where date = ?', (str(self.selected_date),)):
            return DailyFood(row[0], row[1], row[2], row[3])
    
    def update_weight(self, weight):
        logger.info("Updating weight: " + str(weight))
        self.cursor.execute('UPDATE daily_food SET weight = ? WHERE date = ?', (str(weight), str(self.selected_date)))
        self.conn.commit()

    def delete_xref_daily_food(self):
        logger.info("Deleting xref daily food")
        self.cursor.execute('DELETE FROM xref_daily_foods WHERE id = ?', (self.selected_xref_id,))
        self.conn.commit()

    def add_xref_daily_food(self, daily_food_id, name, fat, protein, carb, calories):
        logger.info("Adding xref daily food")
        self.cursor.execute('INSERT INTO xref_daily_foods (daily_food_id, name, fat, protein, carb, calories) VALUES (?, ?, ?, ?, ?, ?)', (str(daily_food_id), name, fat, protein, carb, calories))
        self.conn.commit()

    def get_xref_daily_foods(self, daily_food_id):
        logger.info("Getting xref daily foods")
        xref_daily_foods = []
        for row in self.cursor.execute('SELECT * FROM xref_daily_foods WHERE daily_food_id = ?', (str(daily_food_id),)):
            xref_daily_foods.append(XrefDailyFood(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return xref_daily_foods