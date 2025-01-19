import random

from faker import Faker

fake = Faker()

PL_pet_id = fake.random_number(8)
category_id = fake.random_number(8)
category_name = fake.language_name()
pet_name = fake.first_name()
photo_url = fake.url()
tag_id = fake.random_number(8)
tag_name = fake.color_name()
status_random = random.choice(["available", "pending", "sold"])

class Payloads:

    PL_add_pet = {
  "id": PL_pet_id,
  "category": {
    "id": category_id,
    "name": category_name
  },
  "name": pet_name,
  "photoUrls": [
    photo_url
  ],
  "tags": [
    {
      "id": tag_id,
      "name": tag_name
    }
  ],
  "status": status_random
}

    PL_update_pet_fully = {
      "id": PL_pet_id,
      "category": {
        "id": category_id,
        "name": category_name
      },
      "name": pet_name + " UPDATE 1",
      "photoUrls": [
        photo_url
      ],
      "tags": [
        {
          "id": tag_id,
          "name": tag_name
        }
      ],
      "status": status_random
    }