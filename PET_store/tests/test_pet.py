from PET_store.config.base_test import BaseTest



class TestPet (BaseTest):

    def test_add_pet (self):
        self.api_pet.add_pet()