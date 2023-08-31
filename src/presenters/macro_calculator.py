from src import app_logging

logger = app_logging.get_app_logger(__name__)

class CalculatedMacros:
    def __init__(self, fat_grams, protein_grams, carb_grams, calories):
        self.fat_grams = fat_grams
        self.protein_grams = protein_grams
        self.carb_grams = carb_grams
        self.calories = calories

class MacroCalculator:
    def calculate_food_macros(self, food, multiplier):
        logger.debug("Calculating food macros with multiplier: " + str(multiplier))
        calculated_macros = CalculatedMacros(0, 0, 0, 0)
        fat_calories = (food.fat * 9) * float(multiplier)
        protein_calories = (food.protein * 4) * float(multiplier)
        carbs_calories = (food.carbs * 4) * float(multiplier)
        
        calculated_macros.calories = round(fat_calories + protein_calories + carbs_calories)
        calculated_macros.fat_grams = round(food.fat * float(multiplier))
        calculated_macros.protein_grams = round(food.protein * float(multiplier))
        calculated_macros.carbs_grams = round(food.carbs * float(multiplier))

        logger.debug("Calculated macros: " + str(calculated_macros.fat_grams) + ", " + str(calculated_macros.protein_grams) + ", " + str(calculated_macros.carbs_grams) + ", " + str(calculated_macros.calories))
        return calculated_macros

    def calculate_fat_protein_carb_grams(self, ingredients):
        total_fat_grams = 0
        total_protein_grams = 0
        total_carb_grams = 0
        for i in ingredients:
            total_fat_grams += (i.food.fat * i.unit_multiplier)
            total_protein_grams += (i.food.protein * i.unit_multiplier)
            total_carb_grams += (i.food.carbs * i.unit_multiplier)
        return total_fat_grams, total_protein_grams, total_carb_grams

    def calculate_recipe_macros(self, servings, ingredients, multiplier):
        logger.debug("Calculating recipe macros with multiplier: " + str(multiplier))
        calculated_macros = CalculatedMacros(0, 0, 0, 0)
        results = self.calculate_fat_protein_carb_grams(ingredients)
        calculated_macros = CalculatedMacros(0, 0, 0, 0)
        calculated_macros.fat_grams = (results[0] / float(servings)) * float(multiplier)
        calculated_macros.protein_grams = (results[1] / float(servings)) * float(multiplier)
        calculated_macros.carb_grams = (results[2] / float(servings)) * float(multiplier)

        fat_calories = (calculated_macros.fat_grams * 9)
        protein_calories = (calculated_macros.protein_grams * 4)
        carbs_calories = (calculated_macros.carb_grams * 4)
        calculated_macros.calories = fat_calories + protein_calories + carbs_calories

        return calculated_macros

    def get_goal_fat_grams(self, goal, bonus):
        fat_calories = (float(goal.fat_percent) * (float(goal.bmr_calories) + float(bonus))) / 100
        fat_grams = fat_calories / 9
        return int(round(fat_grams))

    def get_goal_protein_grams(self, goal, bonus):
        protein_calories = (float(goal.protein_percent) * (float(goal.bmr_calories) + float(bonus))) / 100
        protein_grams = protein_calories / 4
        return int(round(protein_grams))

    def get_goal_carb_grams(self, goal, bonus):
        carbs_calories = (float(goal.carbs_percent) * (float(goal.bmr_calories) + float(bonus))) / 100
        carbs_grams = carbs_calories / 4
        return int(round(carbs_grams))

    def get_goal_calories(self, goal, bonus):
        calories = (float(goal.bmr_calories) + float(bonus))
        return calories

    def calculate_fat_percent(self, fat_g, total_calories):
        logger.debug("Calculating fat percent with: " + str(fat_g) + ", " + str(total_calories))
        percent_fat = 0
        total_calories_f = float(total_calories)
        fat_g_f = float(fat_g)
        if fat_g > 0:
            fat_calories = total_calories_f - (total_calories_f - (fat_g_f * 9))
            percent_fat = (fat_calories / total_calories_f) * 100
        return int(round(percent_fat))

    def calculate_protein_percent(self, protein_g, total_calories):
        percent_protein = 0
        total_calories_p = float(total_calories)
        protein_g_p = float(protein_g)
        if protein_g > 0:
            protein_calories = total_calories_p - (total_calories_p - (protein_g_p * 4))
            percent_protein = (protein_calories / total_calories_p) * 100
        return int(round(percent_protein))

    def calculate_carb_percent(self, carb_g, total_calories):
        percent_carb = 0
        total_calories_c = float(total_calories)
        carb_g_c = float(carb_g)
        if carb_g > 0:
            carb_calories = total_calories_c - (total_calories_c - (carb_g_c * 4))
            percent_carb = (carb_calories / total_calories_c) * 100
        return int(round(percent_carb))
