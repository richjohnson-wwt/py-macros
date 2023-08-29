import unittest

import sys
sys.path.append('src/presenters')
sys.path.append('src/models')

import macro_calculator
import food_model

class TestMacroCalculator(unittest.TestCase):
    def test_calculate_evoo_with_multiplier(self):
        test_object = macro_calculator.MacroCalculator()
        evoo = food_model.Food(1, "EVOO", 14, 0, 0, 120, 1, 5, 11)
        cm = test_object.calculate_food_macros(evoo, 2)
        self.assertEqual(cm.fat_grams, 28)