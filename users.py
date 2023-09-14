from locust import TaskSet, task, between
from faker import Faker

class UserRouteLoadTest(TaskSet):
    faker = Faker("pt_br")
    wait_time = between(1, 5)

    @task
    def get_list_users(self):
        self.client.get("/usuarios", name="Obter Usuários Cadastrados")

    @task
    def post_created_user(self):
        response = self.client.post("/usuarios", name="Criar Usuários",
                         json={
                            "nome": self.faker.name(),
                            "email": self.faker.email(),
                            "password": "teste",
                            "administrador": "true"
                            }
                        )
        # print( response.content )