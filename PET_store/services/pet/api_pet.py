import requests

from PET_store.config.headers import Headers
from PET_store.services.pet.endpoints import Endpoints
from PET_store.services.pet.payloads import Payloads


class PetAPI:

    def __init__(self):
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    def add_pet (self):
        response = requests.post(
            url = self.endpoints.add_pet,
            headers = self.headers.accept_json,
            json = self.payloads.add_pet
        )
        print(response.json())
        assert response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {response.status_code}"