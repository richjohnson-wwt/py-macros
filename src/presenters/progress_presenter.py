
from datetime import datetime, timedelta

from src import app_logging

from weight_loss_projector import WeightLossProjector

logger = app_logging.get_app_logger(__name__)

DATE_FORMAT = "%Y-%m-%d"

class ProgressPresenter:
    def __init__(self, daily_model, goal_model, view, macro_calculator, daily_view):
        self.daily_model = daily_model
        self.goal_model = goal_model
        self.view = view
        self.daily_view = daily_view
        self.macro_calculator = macro_calculator
        self.daily_model.register(self)
        self.is_listening = False

    def post_init(self):
        self.is_listening = True
        self.update()

    def update(self):
        if self.is_listening:
            self.populate_calorie_section()
            self.populate_progress_date()
            self.populate_goal_date()
            self.populate_actual_weight_diff()
            self.populate_macro_chart()

    def populate_macro_chart(self):
        logger.debug("====Populating macro chart====")
        bonus_calories = self.daily_view.add_activity_text_ctrl.GetValue()
        goal = self.goal_model.get_goal()
        goal_fat_grams = self.macro_calculator.get_goal_fat_grams(goal, bonus_calories)
        goal_protein_grams = self.macro_calculator.get_goal_protein_grams(goal, bonus_calories)
        goal_carb_grams = self.macro_calculator.get_goal_carb_grams(goal, bonus_calories)
        goal_calories = self.macro_calculator.get_goal_calories(goal, bonus_calories)

        totals_list = self.daily_model.get_totals(bonus_calories, goal, goal_fat_grams, goal_protein_grams, goal_carb_grams, goal_calories)

        totals = totals_list[2]
        total_fat = totals.fat
        total_protein = totals.protein
        total_carb = totals.carbs
        total_calories = totals.calories
        percent_fat = self.macro_calculator.calculate_fat_percent(total_fat, total_calories)
        percent_protein = self.macro_calculator.calculate_protein_percent(total_protein, total_calories)
        percent_carb = self.macro_calculator.calculate_carb_percent(total_carb, total_calories)
        labels = 'Fat', 'Protein', 'Carbs'
        sizes = [percent_fat, percent_protein, percent_carb]
        logger.debug("Fat: " + str(percent_fat) + " Protein: " + str(percent_protein) + " Carbs: " + str(percent_carb))
        # if all of the percent values are NOT 0, then draw the chart
        if percent_fat > 0 or percent_protein > 0 or percent_carb > 0:
            self.view.draw_chart(labels, sizes)
        else:
            self.view.draw_chart(labels, [1, 1, 1])
        
    def populate_calorie_section(self):
        dt_end_date = datetime.strptime(self.daily_model.get_today_date(), DATE_FORMAT)
        time_delta = timedelta(days=7)
        dt_start_date = dt_end_date - time_delta
        daily_foods_by_date_range = self.daily_model.get_daily_food_by_date_range(dt_start_date, dt_end_date)
        exercise_calories = 0
        xref_daily_foods = []
        for daily_food in daily_foods_by_date_range:
            exercise_calories += daily_food.exercise
            xref_daily_foods += self.daily_model.get_xref_daily_foods(daily_food.daily_food_id)
        self.view.activity_calories_text_ctrl.SetValue(str(exercise_calories))

        total_calories = 0
        for xref_daily_food in xref_daily_foods:
            total_calories += xref_daily_food.calories
        self.view.consumed_calories_text_ctrl.SetValue(str(total_calories))

        bmr = self.goal_model.get_goal().bmr_calories
        seven_days_calories = bmr * 7
        seven_days_calories_plus_exercise = round(seven_days_calories + exercise_calories, 2)
        deficit = seven_days_calories_plus_exercise - total_calories
        pounds_lost = round(deficit / 3500, 2) * -1
        self.view.expected_weight_delta_text_ctrl.SetValue(str(pounds_lost))
        self.view.bmr_plus_exercise_text_ctrl.SetValue(str(seven_days_calories_plus_exercise))
        self.view.net_in_out_text_ctrl.SetValue(str(deficit))
        pass

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

    def populate_actual_weight_diff(self):
        dt_end_date = datetime.strptime(self.daily_model.get_today_date(), DATE_FORMAT)
        time_delta = timedelta(days=7)
        dt_start_date = dt_end_date - time_delta

        logger.debug("start_date: " + str(dt_start_date) + " end_date: " + str(dt_end_date))

        daily_foods_by_date_range = self.daily_model.get_daily_food_by_date_range(dt_start_date, dt_end_date)
        weights = []
        for daily_food in daily_foods_by_date_range:
            if daily_food.weight > 0:
                weights.append(daily_food.weight)

        first_weight = 0
        first_done = False
        last_weight = 0
        for weight in weights:
            if weight > first_weight:
                if not first_done:
                    first_weight = weight
                    first_done = True
            last_weight = weight
        logger.debug("First weight: " + str(first_weight) + " Last weight: " + str(last_weight))
        weight_diff = last_weight - first_weight
        self.view.actual_weight_diff_text_ctrl.SetValue("{:.1f}".format(weight_diff))
