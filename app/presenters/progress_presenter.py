
from datetime import datetime, timedelta

from app import app_logging

from weight_loss_projector import WeightLossProjector

logger = app_logging.get_app_logger(__name__)

DATE_FORMAT = "%Y-%m-%d"

class ProgressPresenter:
    def __init__(self, daily_model, goal_model, view):
        self.daily_model = daily_model
        self.goal_model = goal_model
        self.view = view

    def post_init(self):
        self.populate_progress_date()
        self.populate_goal_date()
        
    def populate_goal_date(self):
        end_date = self.daily_model.get_today_date()
        start_date = self.goal_model.get_goal().start_date

        dt_start = datetime.strptime(start_date, DATE_FORMAT)
        dt_end = datetime.strptime(end_date, DATE_FORMAT)
        days_elapsed = dt_end - dt_start

        logger.debug("Days Elapsed: " + str(days_elapsed.days))
        daily_foods_by_date_range = self.daily_model.get_daily_food_by_date_range(start_date, end_date)
        first_weight = daily_foods_by_date_range[0].weight
        target_weight = self.goal_model.get_goal().target_weight

        weights = []
        steady_weight_increment = first_weight
        while steady_weight_increment > target_weight:
            weights.append(steady_weight_increment)
            steady_weight_increment -= 0.165

        weight_loss_projector = WeightLossProjector(weights)
        weight_loss_projector.calculate()

        _number_of_weeks_to_reach_goal = weight_loss_projector.number_of_weeks_to_reach_goal(target_weight)

        time_delta = timedelta(days=(_number_of_weeks_to_reach_goal * 7))
        dt_start_date = datetime.strptime(self.goal_model.get_goal().start_date, DATE_FORMAT)
        future_goal_date = dt_start_date + time_delta

        self.view.goal_date_text_ctrl.SetValue(str(future_goal_date.strftime(DATE_FORMAT)))


    def populate_progress_date(self):
        end_date = self.daily_model.get_today_date()
        start_date = self.goal_model.get_goal().start_date

        dt_start = datetime.strptime(start_date, DATE_FORMAT)
        dt_end = datetime.strptime(end_date, DATE_FORMAT)
        days_elapsed = dt_end - dt_start

        logger.debug("Days Elapsed: " + str(days_elapsed.days))
        logger.debug("Date range is: " + str(start_date) + " to " + str(end_date))
        daily_foods_by_date_range = self.daily_model.get_daily_food_by_date_range(start_date, end_date)
        logger.debug("Daily foods by date range: " + str(len(daily_foods_by_date_range)))
        weights = []
        for daily_food in daily_foods_by_date_range:
            if daily_food.weight > 0:
                weights.append(daily_food.weight)

        weight_loss_projector = WeightLossProjector(weights)
        weight_loss_projector.calculate()

        _slope = weight_loss_projector.slope
        _intercept = weight_loss_projector.intercept

        logger.debug("Slope: " + str(_slope) + " Intercept: " + str(_intercept))

        _number_of_weeks_to_reach_goal = weight_loss_projector.number_of_weeks_to_reach_goal(self.goal_model.get_goal().target_weight)
        logger.debug("Number of weeks to reach goal: " + str(_number_of_weeks_to_reach_goal))
        percentage_of_weights_to_elapsed_days = len(daily_foods_by_date_range) / days_elapsed.days
        number_of_weeks_normalized = _number_of_weeks_to_reach_goal / percentage_of_weights_to_elapsed_days
        logger.debug("Number of weeks normalized: " + str(number_of_weeks_normalized))

        time_delta = timedelta(days=(number_of_weeks_normalized * 7))
        dt_start_date = datetime.strptime(self.goal_model.get_goal().start_date, DATE_FORMAT)
        future_goal_date = dt_start_date + time_delta

        self.view.progress_date_text_ctrl.SetValue(str(future_goal_date.strftime(DATE_FORMAT)))
