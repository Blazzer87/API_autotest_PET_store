import json
import pytest
from config.base_test import BaseTest
from model.pet_json_model import PetJsonModel, StatusMessageModel


class TestUserFlowCRUD (BaseTest):


    # @pytest.fixture
    # def create_pet_data(self):
    #     return {'id': 9223372036854742, 'category': {'id': 111111111, 'name': 'FIRSTcategory'}, 'name': 'FIRSTname', 'photoUrls': ['http://FIRTSurl.ru'], 'tags': [{'id': 22222222, 'name': 'FIRSTtag'}], 'status': 'available'}


    @pytest.fixture
    def create_pet_data(self):
        return 9223372036854742, 11111111, 'FIRSTcategory', 'FIRSTname', 'http://FIRTSurl.ru', 22222222, 'FIRSTtag', 'available'


    @pytest.fixture
    def update_pet_data(self):
        return 9223372036854742, 99999999, "SECONDcategory", "SECONDname", "http://SECONDurl.ru", 88888888, "SECONDtag", "pending"


    # @pytest.fixture(autouse=True)
    # def get_pet_data(self, create_pet_data):
    #     self.pet_id = create_pet_data['id']
    #     self.category_id = create_pet_data['category']['id']
    #     self.category_name = create_pet_data['category']['name']
    #     self.pet_name = create_pet_data['name']
    #     self.photo_url = create_pet_data['photoUrls'][0]
    #     self.tag_id = create_pet_data['tags'][0]['id']
    #     self.tag_name = create_pet_data['tags'][0]['name']
    #     self.status = create_pet_data['status']


    def test_add_pet(self, create_pet_data):
        self.response = self.api_pet.add_pet(*create_pet_data)
        # проверяем соответствие отправленного в запросе тела и полученного тела в ответе
        assert json.loads(self.response.request.body.decode('utf-8')) == self.response.json(), f"Полученный ответ не соответствует отправленным данным"
        # проверяем статус код
        assert self.response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {self.response.status_code}"
        print("\nПолученный ответ:\n", self.response.json())
        # валидируем модель на соответствие типам данных
        PetJsonModel(**self.response.json())


    def test_find_pet (self, create_pet_data):
        self.response = self.api_pet.find_pet_by_id(pet_id=create_pet_data[0])
        assert self.response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {self.response.status_code}"
        print("\nПолученный ответ:\n", self.response.json())
        PetJsonModel(**self.response.json())


    def test_update_pet_fully (self, update_pet_data):
        self.response = self.api_pet.update_pet_fully(*update_pet_data)
        assert json.loads(self.response.request.body.decode('utf-8')) == self.response.json(), f"Полученный ответ не соответствует отправленным данным"
        assert self.response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {self.response.status_code}"
        print("\nПолученный ответ:\n", self.response.json())
        PetJsonModel(**self.response.json())


    @pytest.mark.parametrize('name, status', [('`THIRDname`', 'sold')])
    def test_update_pet_by_id (self, update_pet_data, name, status):
        self.response = self.api_pet.update_pet_by_id(pet_id=update_pet_data[0], name_data=name, status_data=status)
        assert self.response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {self.response.status_code}"
        print("\nПолученный ответ:\n", self.response.json())
        StatusMessageModel(**self.response.json())


    def test_find_pet_retry (self, create_pet_data):
        self.response = self.api_pet.find_pet_by_id(pet_id=create_pet_data[0])
        assert self.response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {self.response.status_code}"
        print("\nПолученный ответ:\n", self.response.json())
        PetJsonModel(**self.response.json())


    def test_delete_pet (self, create_pet_data):
        self.response = self.api_pet.delete_pet(pet_id=create_pet_data[0])
        assert self.response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {self.response.status_code}"
        print("\nПолученный ответ:\n", self.response.json())
        StatusMessageModel(**self.response.json())
