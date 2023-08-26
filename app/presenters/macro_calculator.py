from app import app_logging

logger = app_logging.get_app_logger(__name__)

class CalculatedMacros:
    def __init__(self, fat_grams, protein_grams, carb_grams, calories):
        self.fat_grams = fat_grams
        self.protein_grams = protein_grams
        self.carb_grams = carb_grams
        self.calories = calories

class MacroCalculator:
    def calculate_food_macros(self, food, multiplier):
        logger.info("Calculating food macros with multiplier: " + str(multiplier))
        calculated_macros = CalculatedMacros(0, 0, 0, 0)
        fat_calories = (food.fat * 9) * float(multiplier)
        protein_calories = (food.protein * 4) * float(multiplier)
        carbs_calories = (food.carbs * 4) * float(multiplier)
        calculated_macros.calories = fat_calories + protein_calories + carbs_calories

        calculated_macros.fat_grams = food.fat * float(multiplier)
        calculated_macros.protein_grams = food.protein * float(multiplier)
        calculated_macros.carbs_grams = food.carbs * float(multiplier)

        logger.info("Calculated macros: " + str(calculated_macros.fat_grams) + ", " + str(calculated_macros.protein_grams) + ", " + str(calculated_macros.carbs_grams) + ", " + str(calculated_macros.calories))
        return calculated_macros