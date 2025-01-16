from PET_store.services.pet.api_pet import PetAPI


class BaseTest:

    def setup (self):
        self.api_pet = PetAPI()