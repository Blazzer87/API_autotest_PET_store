import pytest
from faker import Faker

from pet_service.api_pet import PetAPI


class BaseTest:

    api_pet = None
    faker = None

    @pytest.fixture(autouse=True)
    def setup (self):
        self.api_pet = PetAPI()
        self.faker = Faker()