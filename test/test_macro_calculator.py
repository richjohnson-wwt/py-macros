import unittest

import sys
sys.path.append('src/presenters')
sys.path.append('src/models')


import macro_calculator
import food_model
import unit_model
import recipe_model
import goal_model

class TestMacroCalculator(unittest.TestCase):
    def test_calculate_evoo_with_multiplier(self):
        test_object = macro_calculator.MacroCalculator()
        evoo = food_model.Food(1, "EVOO", 14, 0, 0, 120, 1, 5, 11)
        cm = test_object.calculate_food_macros(evoo, 2)
        self.assertEqual(cm.fat_grams, 28)

    def test_calculate_fat_protein_carb_grams(self):
        test_object = macro_calculator.MacroCalculator()
        evoo = food_model.Food(1, "EVOO", 14, 0, 0, 120, 1, 5, 11)
        parm = food_model.Food(2, "Parmesan", 8, 9, 1, 120, 1, 1, 0)
        tbsp = unit_model.Unit(1, "tbsp")
        grams = unit_model.Unit(2, "grams")
        evoo_ingredient = recipe_model.Ingredient(evoo, 2, tbsp)
        parm_ingredient = recipe_model.Ingredient(parm, 2, grams)
        ingredients = [evoo_ingredient, parm_ingredient]
        total_fat_grams, total_protein_grams, total_carb_grams = test_object.calculate_fat_protein_carb_grams(ingredients)
        self.assertEqual(total_fat_grams, 44)
        self.assertEqual(total_protein_grams, 18)
        self.assertEqual(total_carb_grams, 2)

    def test_calculate_recipe_macros(self):
        test_object = macro_calculator.MacroCalculator()
        evoo = food_model.Food(1, "EVOO", 14, 0, 0, 120, 1, 5, 11)
        parm = food_model.Food(2, "Parmesan", 8, 9, 1, 120, 1, 1, 0)
        tbsp = unit_model.Unit(1, "tbsp")
        grams = unit_model.Unit(2, "grams")
        evoo_ingredient = recipe_model.Ingredient(evoo, 2, tbsp)
        parm_ingredient = recipe_model.Ingredient(parm, 2, grams)
        ingredients = [evoo_ingredient, parm_ingredient]
        servings = 2
        multiplier = 2
        calculated_macros = test_object.calculate_recipe_macros(servings, ingredients, multiplier)
        self.assertEqual(calculated_macros.fat_grams, 44)
        self.assertEqual(calculated_macros.protein_grams, 18)
        self.assertEqual(calculated_macros.carb_grams, 2)

    def test_get_goal_fat_grams(self):
        test_object = macro_calculator.MacroCalculator()
        goal = goal_model.Goal(1, "2023-08-29", 155, 1702, 75, 20, 5)
        bonus = 300
        fat_grams = test_object.get_goal_fat_grams(goal, bonus)
        self.assertEqual(fat_grams, 167)

    def test_get_protein_grams(self):
        test_object = macro_calculator.MacroCalculator()
        goal = goal_model.Goal(1, "2023-08-29", 155, 1702, 75, 20, 5)
        bonus = 300
        protein_grams = test_object.get_goal_protein_grams(goal, bonus)
        self.assertEqual(protein_grams, 100)

    def test_get_carb_grams(self):
        test_object = macro_calculator.MacroCalculator()
        goal = goal_model.Goal(1, "2023-08-29", 155, 1702, 75, 20, 5)
        bonus = 300
        carb_grams = test_object.get_goal_carb_grams(goal, bonus)
        self.assertEqual(carb_grams, 25)

    def test_calculate_fat_percent(self):
        test_object = macro_calculator.MacroCalculator()
        fat_g = 166
        total_calories = 2002
        fat_percent = test_object.calculate_fat_percent(fat_g, total_calories)
        self.assertEqual(fat_percent, 75)

    def test_calculate_protein_percent(self):
        test_object = macro_calculator.MacroCalculator()
        protein_g = 100
        total_calories = 2002
        protein_percent = test_object.calculate_protein_percent(protein_g, total_calories)
        self.assertEqual(protein_percent, 20)

    def test_calculate_carb_percent(self):
        test_object = macro_calculator.MacroCalculator()
        carb_g = 25
        total_calories = 2002
        carb_percent = test_object.calculate_carb_percent(carb_g, total_calories)
        self.assertEqual(carb_percent, 5)