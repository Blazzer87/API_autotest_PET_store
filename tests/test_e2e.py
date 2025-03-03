import pytest
from pytest_lazyfixture import lazy_fixture

from config.base_test import BaseTest
from json_example.pet_json import PetJsonModel


class TestUserFlowCRUD (BaseTest):

    @pytest.fixture
    def create_pet_data(self):
        return 28022025, 90909009, "categorname", "ЁЖИК", "http://nofoto.ru", 123456789, "thisisTagName", "available"

    @pytest.fixture
    def update_pet_data(self):
        return 11111111, 922222222, "categorname2", "ЙОЖЕГ", "http://nofoto.ru", 987654321, "TagNamethisis", "sold"


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



    # def test_update_pet_by_id (self):
    #     self.api_pet.update_pet_by_id()
    #
    #
    # def test_find_pet_retry (self):
    #     var = self.api_pet.find_pet_by_ID()
    #     print("Мы обновили имя на: ", var.name, '\n')
    #
    #
    # def test_delete_pet (self):
    #     self.api_pet.delete_pet()
    #
    #
    # def test_check_delete_pet (self):
    #     self.api_pet.check_del_pet_by_ID()
    #


