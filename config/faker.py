import random

from faker import Faker

from config.base_test import BaseTest



def generate_pet_data():
    faker = Faker()
    pet_id =  random.randint(11111111,99999999)
    category_id = random.randint(111111,999999)
    category_name = faker.first_name()
    pet_name = faker.first_name()
    photo_url = faker.url()
    tag_id = random.randint(111111,999999)
    tag_name = faker.color_name()
    status = random.choice(('available','pending', 'sold'))
    print(pet_id)
    print(category_id)
    print(category_name)
    print(pet_name)
    print(photo_url)
    print(tag_id)
    print(tag_name)
    print(status)

generate_pet_data()




