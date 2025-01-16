import random

from faker import Faker

fake = Faker()

class Payloads:

    add_pet = {
  "id": fake.random_number(8),
  "category": {
    "id": fake.random_number(8),
    "name": f"{fake.language_name()}"
  },
  "name": f"{fake.first_name()}",
  "photoUrls": [
    f"{fake.url()}"
  ],
  "tags": [
    {
      "id": fake.random_number(8),
      "name": f"{fake.color_name()}"
    }
  ],
  "status": f"{random.choice(["available", "pending", "sold"])}"
}


