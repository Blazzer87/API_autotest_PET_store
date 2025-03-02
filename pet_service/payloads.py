import pytest


class Payloads:

    def payload_add_pet(self, pet_id, category_id, category_name, pet_name, photo_url, tag_id, tag_name, status):
        return {"id": pet_id,
                "category": {"id": category_id,"name": category_name},
                "name": pet_name,
                "photoUrls": [photo_url],
                "tags": [{"id": tag_id,"name": tag_name}],
                "status": status
                }