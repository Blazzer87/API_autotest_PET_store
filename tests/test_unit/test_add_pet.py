# import pytest
# from config.base_test import BaseTest
# from model.pet_json_model import PetJsonModel, StatusMessageModel
#
#
# class TestAddPet (BaseTest):
#
#     #
#     # add_pet_data= (9223372036854742, 111111111, "categorЁЖИК", "ЁЖИК", "http://ЁЖИК.ru", 22222222, "thisisTagName", "available")
#     #
#     #
#     # @pytest.mark.parametrize(create_pet_data)
#     # def test_add_pet(self, create_pet_data):
#     #     self.response = self.api_pet.add_pet(*create_pet_data)
#     #     assert self.response.status_code == 200, f"Статус-код отличается от ожидаемого. Получен код {self.response.status_code}"
#     #     print("\nПолученный ответ:\n", self.response.json())
#     #     PetJsonModel(**self.response.json())