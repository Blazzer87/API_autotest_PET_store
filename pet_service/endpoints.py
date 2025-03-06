
HOST = "https://petstore.swagger.io/v2"

class Endpoints:

    EP_upload_image_pet = lambda self, EP_pet_id: f"{HOST}/pet/{EP_pet_id}/uploadImage"

    EP_find_by_status_pet = f"{HOST}/pet/findByStatus"


    def endpoint_add_pet(self):
        return f"{HOST}/pet"

    def endpoint_update_pet_fully(self):
        return f"{HOST}/pet"

    def endpoint_find_pet_by_id(self, pet_id):
        return f"{HOST}/pet/{pet_id}"

    def endpoint_update_pet_by_id(self, pet_id):
        return f"{HOST}/pet/{pet_id}"

    def endpoint_delete_pet_by_id(self, pet_id):
        return f"{HOST}/pet/{pet_id}"