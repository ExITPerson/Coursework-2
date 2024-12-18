import pytest
import json


@pytest.fixture
def job_json():
    data = {'items': [
        {'id': '111325640', 'premium': False, 'name': 'Менеджер по продажам', 'department': None, 'has_test': False}]}

    return json.dumps(data)
