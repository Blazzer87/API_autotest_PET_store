import requests

from pet_service.headers import Headers
from pet_service.endpoints import Endpoints
from pet_service.payloads import *
from json_example.pet_json import PetJSON



class PetAPI:


    def __init__(self):
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()


    def add_pet (self):

        response = requests.post(
            url = self.endpoints.EP_add_pet,
            headers = self.headers.headers_acceptjson_contentjson,
            json = self.payloads.PL_add_pet
        )
        print(response.json())
        assert response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {response.status_code}"
        model = PetJSON(**response.json())
        return model


    def find_pet_by_ID (self):

        response = requests.get(
            url = self.endpoints.EP_find_by_ID_pet(EP_pet_id=PL_pet_id),
            headers = self.headers.headers_acceptjson_contentjson
        )
        print(response.json())
        assert response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {response.status_code}"
        model = PetJSON(**response.json())
        return model


    def update_pet_fully (self):

        response = requests.put(
            url=self.endpoints.EP_update_pet_fully,
            headers=self.headers.headers_acceptjson_contentjson,
            json=self.payloads.PL_update_pet_fully
        )
        print(response.json())
        assert response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {response.status_code}"
        model = PetJSON(**response.json())
        return model


    def update_pet_by_id (self):

        x_www_form_urlencoded = {
            'name': pet_name + " UPDATE 2",
            'status': 'sold'
        }
        response = requests.post(
            url=self.endpoints.EP_update_name_and_status_pet(EP_pet_id=PL_pet_id),
            headers=self.headers.headers_acceptjson_contentxwwwformurlencoded,
            data= x_www_form_urlencoded
        )
        print(response.json())
        assert response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {response.status_code}"


    def delete_pet (self):

        response = requests.delete(
            url=self.endpoints.EP_delete_pet(EP_pet_id=PL_pet_id),
            headers=self.headers.headers_acceptjson_contentjson
        )
        print(response.json())
        assert response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {response.status_code}"


    def check_del_pet_by_ID (self):

        response = requests.get(
            url = self.endpoints.EP_find_by_ID_pet(EP_pet_id=PL_pet_id),
            headers = self.headers.headers_acceptjson_contentjson
        )
        print(response.json())
        assert response.status_code == 404, f"Статус-код отличается от ожидаемого. Получен код {response.status_code}"
