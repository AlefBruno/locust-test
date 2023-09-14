from locust import TaskSet, task
from faker import Faker

class UserRouteLoadTest(TaskSet):
    faker = Faker()

    @task
    def get_list_users(self):
        self.client.get("/usuarios", name="Obter Usuários Cadastrados")

    @task
    def post_created_user(self):
        name = self.faker.name()
        self.client.post("/usuarios", name="Criar Usuários",
                         json={
                            "nome": f"{name}",
                            "email": f"{name.split()[0]}@qa.com.br",
                            "password": "teste",
                            "administrador": "true"
                            }
                        )