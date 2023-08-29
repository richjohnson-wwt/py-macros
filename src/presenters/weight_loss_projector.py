
from src import app_logging

logger = app_logging.get_app_logger(__name__)

class WeightLossProjector:
    def __init__(self, weights):
        self.y_values = weights

    def calculate(self):
        _x = []
        _xy = []
        _x2 = []
        for i in range(1, len(self.y_values) + 1):
            logger.info("i: " + str(i) + " y: " + str(self.y_values[i - 1]))
            _x.append(i)
            _xy.append(i * self.y_values[i - 1])
            _x2.append(i * i)

        _sum_x = sum(_x)
        _sum_y = sum(self.y_values)
        _sum_xy = sum(_xy)
        _sum_x2 = sum(_x2)

        logger.debug("Sum X: " + str(_sum_x))
        logger.debug("Sum Y: " + str(_sum_y))
        logger.debug("Sum XY: " + str(_sum_xy))
        logger.debug("Sum X2: " + str(_sum_x2))

        n = len(self.y_values)
        self.slope = ((n * _sum_xy) - (_sum_x * _sum_y)) / ((n * _sum_x2) - (_sum_x * _sum_x))
        self.intercept = (_sum_y - (self.slope * _sum_x)) / n

    def weight_at_day(self, day):
        return (self.slope * day) + self.intercept

    def number_of_weeks_to_reach_goal(self, goal):
        return int(round(((int(goal) - self.intercept) / self.slope) / 7))

    def sum(self, values):
        values_sumed = 0
        for i in values:
            values_sumed += i
        return values_sumed
