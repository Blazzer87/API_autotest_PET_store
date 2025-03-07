import json
import random
import pytest
from pydantic import ValidationError
from contextlib import nullcontext as does_not_raises
from config.base_test import BaseTest
from model.pet_json_model import PetJsonModel, StatusMessageModel




class TestMethodAdd (BaseTest):

    @staticmethod
    def random_id():
        random_id = int(random.randint(11111111, 99999999))
        return random_id


    custom_payload = [

        # test 1
        ({"id": random_id(), "category": {"id": random_id(), "name": "FIRSTcategory"}, "name": "FIRSTname", "photoUrls": ["http://FIRTSurl.ru"], "tags": [{"id": random_id(), "name": "FIRSTtag"}], "status": "available"},
        does_not_raises(), [200,201]),

        # test 2
        ({"name": "FIRSTname", "photoUrls": ["http://FIRTSurl.ru"]},
         does_not_raises(), [200,201]),

        # test 3
        ({"id": 0, "category": {"id": random_id(), "name": "FIRSTcategory"}, "name": "FIRSTname", "photoUrls": ["http://FIRTSurl.ru"], "tags": [{"id": random_id(), "name": "FIRSTtag"}], "status": "available"},
         does_not_raises(), [200,201]),

        # test 4
        ({"category": {"id": random_id(), "name": "FIRSTcategory"}, "name": "FIRSTname", "photoUrls": ["http://FIRTSurl.ru"], "tags": [{"id": random_id(), "name": "FIRSTtag"}], "status": "available"},
         does_not_raises(), [200,201]),

        # test 5
        ({"id": random_id(), "category": {"id": random_id(), "name": "FIRSTcategory"}, "photoUrls": ["http://FIRTSurl.ru"], "tags": [{"id": random_id(), "name": "FIRSTtag"}], "status": "available"},
         does_not_raises(), [400, 405]),

        # test 6
        ({"id": random_id(), "category": {"id": random_id(), "name": "FIRSTcategory"}, "name": "FIRSTname", "tags": [{"id": random_id(), "name": "FIRSTtag"}], "status": "available"},
         does_not_raises(), [400, 405]),

        # test 7
        ({},
         does_not_raises(), [400, 405]),

        # test 8
        ({"id": "hello", "category": {"id": random_id(), "name": "FIRSTcategory"}, "name": "FIRSTname", "photoUrls": ["http://FIRTSurl.ru"], "tags": [{"id": random_id(), "name": "FIRSTtag"}], "status": "available"},
         does_not_raises(), [400, 405]),

        # и так далее

    ]


    @pytest.mark.parametrize('payload, expected_result, status_code', custom_payload,
                             ids=['test 1 - all data',
                                  'test 2 - only required field',
                                  'test 3 - id = 0',
                                  'test 4 - without required field id pet',
                                  'test 5 - without required field name pet',
                                  'test 6 - without required field photoUrls',
                                  'test 7 - with empty payload',
                                  'test 8 - pet_id is a string',

                                  # и так далее

                                  ])
    def test_method_add (self, payload, expected_result, status_code):
        with expected_result:
            self.response = self.api_pet.add_pet_with_adaptive_payload(custom_payload=payload)
            print("\nПолученный ответ:\n", self.response.json())
            assert self.response.status_code in status_code, f"Статус-код отличается от ожидаемого. Получен код {self.response.status_code}, вместо ожидаемого {status_code}"
            PetJsonModel(**self.response.json())