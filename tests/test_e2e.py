import pytest
from config.base_test import BaseTest
from model.pet_json_model import PetJsonModel, StatusMessageModel


class TestUserFlowCRUD (BaseTest):

    @pytest.fixture
    def create_pet_data(self):
        return 9223372036854742, 111111111, "categorЁЖИК", "ЁЖИК", "http://ЁЖИК.ru", 22222222, "thisisTagName", "available"

    @pytest.fixture
    def update_pet_data(self):
        return 9223372036854742, 9999999999, "ЙОЖЕГcategor", "ЙОЖЕГ", "http://nЙОЖЕГ.ru", 8888888888, "TagNamethisis", "pending"


    def test_add_pet(self, create_pet_data):
        self.response = self.api_pet.add_pet(*create_pet_data)
        assert self.response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {self.response.status_code}"
        print("\nПолученный ответ:\n", self.response.json())
        PetJsonModel(**self.response.json())


    def test_find_pet (self, create_pet_data):
        self.response = self.api_pet.find_pet_by_id(pet_id=create_pet_data[0])
        assert self.response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {self.response.status_code}"
        print("\nПолученный ответ:\n", self.response.json())
        PetJsonModel(**self.response.json())


    def test_update_pet_fully (self, update_pet_data):
        self.response = self.api_pet.update_pet_fully(*update_pet_data)
        assert self.response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {self.response.status_code}"
        print("\nПолученный ответ:\n", self.response.json())
        PetJsonModel(**self.response.json())


    @pytest.mark.parametrize('name, status', [('`ЁЖ`', 'sold')])
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
