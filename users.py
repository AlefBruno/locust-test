from locust import TaskSet, task

class UserRouteLoadTest(TaskSet):
    def on_start(self):
        print("STARTED !!!")

    @task
    def get_list_users(self):
        self.client.get("/usuarios", name="Obter Usuários Cadastrados")
