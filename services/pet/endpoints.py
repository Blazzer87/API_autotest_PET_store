
HOST = "https://petstore.swagger.io/v2"

class Endpoints:

    upload_image_pet = lambda self, pet_id: f"{HOST}/pet/{pet_id}/uploadImage"
    add_pet = f"{HOST}/pet"
    update_full_pet = f"{HOST}/pet"
    find_by_status_pet = f"{HOST}/pet/findByStatus"
    find_by_ID_pet = lambda self, pet_id: f"{HOST}/pet/{pet_id}"
    update_name_and_status_pet = lambda self, pet_id: f"{HOST}/pet/{pet_id}"
    delete_pet = lambda self, pet_id: f"{HOST}/pet/{pet_id}"