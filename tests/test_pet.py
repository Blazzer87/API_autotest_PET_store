from config.base_test import BaseTest


class TestUserFlowCRUD (BaseTest):

    def test_add_pet (self):
        self.api_pet.add_pet()

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



