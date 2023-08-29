import unittest

import sys
sys.path.append('src/presenters')
sys.path.append('src/models')

import weight_loss_projector

class TestWeightLossProjector(unittest.TestCase):
    def test_calculate(self):
        weights = [200, 190, 192, 188, 187, 186, 186]
        test_object = weight_loss_projector.WeightLossProjector(weights)
        test_object.calculate()
        self.assertAlmostEqual(test_object.weight_at_day(0), 197.71, places=1)
        self.assertAlmostEqual(test_object.weight_at_day(1), 195.75, places=1)
        self.assertAlmostEqual(test_object.weight_at_day(2), 193.78, places=1)
        self.assertAlmostEqual(test_object.weight_at_day(3), 191.82, places=1)
        self.assertAlmostEqual(test_object.weight_at_day(4), 189.85, places=1)
        self.assertAlmostEqual(test_object.weight_at_day(5), 187.89, places=1)
        self.assertAlmostEqual(test_object.weight_at_day(6), 185.92, places=1)

    def test_number_of_weeks_to_reach_goal(self):
        weights = []
        x = 223
        while x > 160:
            weights.append(x)
            x -= 0.2
        test_object = weight_loss_projector.WeightLossProjector(weights)
        test_object.calculate()
        self.assertEqual(45, test_object.number_of_weeks_to_reach_goal(160))