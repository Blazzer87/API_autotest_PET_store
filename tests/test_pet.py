import pytest
from pytest_lazyfixture import lazy_fixture

from config.base_test import BaseTest
from json_example.pet_json import ValidatePetJson


class TestUserFlowCRUD (BaseTest):

    @pytest.fixture
    def create_pet_data(self):
        return 28022025, "090909009", "categorname", "ЁЖИК", "http://nofoto.ru", "123456789", "thisisTagName", "available"


    def test_add_pet(self, create_pet_data):
        self.response = self.api_pet.add_pet(*create_pet_data)
        assert self.response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {self.response.status_code}"
        print(self.response.json())
        ValidatePetJson(**self.response.json())


    def test_find_pet (self):
        self.api_pet.find_pet_by_ID()


    def test_update_pet_fully (self):
        var = self.api_pet.update_pet_fully()
        print("Мы обновили имя на: ", var.name, '\n')


    def test_update_pet_by_id (self):
        self.api_pet.update_pet_by_id()


    def test_find_pet_retry (self):
        var = self.api_pet.find_pet_by_ID()
        print("Мы обновили имя на: ", var.name, '\n')


    def test_delete_pet (self):
        self.api_pet.delete_pet()


    def test_check_delete_pet (self):
        self.api_pet.check_del_pet_by_ID()



