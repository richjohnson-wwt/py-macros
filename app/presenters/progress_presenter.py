

class ProgressPresenter:
    def __init__(self, daily_model, goal_model, view):
        self.daily_model = daily_model
        self.goal_model = goal_model
        self.view = view

    def post_init(self):
        pass