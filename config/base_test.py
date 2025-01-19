import pytest
from pet_service.api_pet import PetAPI


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup (self):
        self.api_pet = PetAPI()