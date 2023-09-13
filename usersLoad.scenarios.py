from locust import HttpUser, LoadTestShape
from users import UserRouteLoadTest

class LoadUsers(HttpUser):
    tasks = [
        UserRouteLoadTest
    ]

class Stages(LoadTestShape):
    stages=[
        {"duration": 30, "users": 30,"spawn_rate": 1,},
        {"duration": 50, "users": 30,"spawn_rate": 1,},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                try:
                    tick_data = (stage["users"], stage["spawn_rate"])
                except:
                    tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data