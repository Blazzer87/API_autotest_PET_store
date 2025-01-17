import pytest

from PET_store.services.pet.api_pet import PetAPI


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup (self):
        self.api_pet = PetAPI()