import requests
from pet_service.headers import Headers
from pet_service.endpoints import Endpoints
from pet_service.payloads import Payloads
from model.pet_json_model import PetJsonModel


class PetAPI:

    response = None

    def __init__(self):
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()


    def add_pet (self, pet_id, category_id, category_name, pet_name, photo_url, tag_id, tag_name, status):

        self.response = requests.post(
            url = self.endpoints.endpoint_add_pet(),
            headers = self.headers.accept_json | self.headers.content_json,
            json = self.payloads.payload_add_pet(pet_id, category_id, category_name, pet_name, photo_url, tag_id, tag_name, status)
        )
        return self.response


    def find_pet_by_id (self, pet_id):

        self.response = requests.get(
            url = self.endpoints.endpoint_find_pet_by_id(pet_id),
            headers = self.headers.accept_json | self.headers.content_json
        )
        return self.response


    def update_pet_fully (self, pet_id, category_id, category_name, pet_name, photo_url, tag_id, tag_name, status):

        self.response = requests.put(
            url=self.endpoints.endpoint_update_pet_fully(),
            headers=self.headers.accept_json | self.headers.content_json,
            json=self.payloads.payload_add_pet(pet_id, category_id, category_name, pet_name, photo_url, tag_id, tag_name, status)
        )
        return self.response


    def update_pet_by_id (self, pet_id, name_data, status_data):

        self.response = requests.post(
            url=self.endpoints.endpoint_update_pet_by_id(pet_id),
            headers=self.headers.accept_json | self.headers.content_x_www_form_urlencoded,
            data={'name': name_data, 'status': status_data}
        )
        return self.response


    def delete_pet (self, pet_id):

        self.response = requests.delete(
            url=self.endpoints.endpoint_update_pet_by_id(pet_id),
            headers=self.headers.accept_json | self.headers.content_json,
        )
        return self.response


    def add_pet_with_adaptive_payload (self, custom_payload):

        self.response = requests.post(
            url = self.endpoints.endpoint_add_pet(),
            headers = self.headers.accept_json | self.headers.content_json,
            json = custom_payload
        )
        return self.response