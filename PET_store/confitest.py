import requests
import pytest

HOST = "https://petstore.swagger.io/v2"

@pytest.fixture(scope="session")
def init_environment ():
    response = requests.post()