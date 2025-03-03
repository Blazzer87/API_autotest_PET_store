import requests

from pet_service.headers import Headers
from pet_service.endpoints import Endpoints
from pet_service.payloads import Payloads
from json_example.pet_json import PetJsonModel


class PetAPI:

    response = None

    def __init__(self):
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()


    def add_pet (self, pet_id, category_id, category_name, pet_name, photo_url, tag_id, tag_name, status):

        self.response = requests.post(
            url = self.endpoints.endpoint_add_pet(),
            headers = self.headers.headers_content_json | self.headers.headers_accept_json_contentjson,
            json = self.payloads.payload_add_pet(pet_id, category_id, category_name, pet_name, photo_url, tag_id, tag_name, status)
        )
        return self.response


    def find_pet_by_id (self, pet_id):

        self.response = requests.get(
            url = self.endpoints.endpoint_find_by_pet_id(pet_id),
            headers = self.headers.headers_content_json | self.headers.headers_accept_json_contentjson
        )
        return self.response


    def update_pet_fully (self, pet_id, category_id, category_name, pet_name, photo_url, tag_id, tag_name, status):

        self.response = requests.put(
            url=self.endpoints.endpoint_update_pet_fully(),
            headers=self.headers.headers_content_json | self.headers.headers_accept_json_contentjson,
            json=self.payloads.payload_add_pet(pet_id, category_id, category_name, pet_name, photo_url, tag_id, tag_name, status)
        )
        return self.response


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
