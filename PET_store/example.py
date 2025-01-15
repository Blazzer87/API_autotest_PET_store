import requests

HOST = "https://petstore.swagger.io/v2"

pet_id = 111111

response = requests.get(
    url = f'{HOST}/pet/{pet_id}')

print(response.status_code)
print(response.json())