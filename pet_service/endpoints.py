
HOST = "https://petstore.swagger.io/v2"

class Endpoints:

    EP_upload_image_pet = lambda self, EP_pet_id: f"{HOST}/pet/{EP_pet_id}/uploadImage"

    EP_update_pet_fully = f"{HOST}/pet"
    EP_find_by_status_pet = f"{HOST}/pet/findByStatus"

    EP_update_name_and_status_pet = lambda self, EP_pet_id: f"{HOST}/pet/{EP_pet_id}"
    EP_delete_pet = lambda self, EP_pet_id: f"{HOST}/pet/{EP_pet_id}"

    def endpoint_add_pet(self):
        return f"{HOST}/pet"

    def endpoint_update_pet_fully(self):
        return f"{HOST}/pet"

    def endpoint_find_by_pet_id(self, pet_id):
        return f"{HOST}/pet/{pet_id}"