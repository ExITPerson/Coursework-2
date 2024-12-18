from src.job_opening import JobOpening
from unittest.mock import patch
import pytest

@patch("requests.get")
def test_job_opening(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'items': [
        {'id': '111325640', 'premium': False, 'name': 'Менеджер по продажам', 'department': None, 'has_test': False}]}
    result = JobOpening()
    assert result.job_openings() == {'items': [
        {'id': '111325640', 'premium': False, 'name': 'Менеджер по продажам', 'department': None, 'has_test': False}]}
    mock_get.assert_called_once_with("https://api.hh.ru/vacancies", params={"period": 90})



@patch("requests.get")
def test_job_opening_error(mock_get):
    mock_get.return_value.status_code = 400
    result = JobOpening()

    with pytest.raises(BaseException, match="Статус код: 400"):
        result.job_openings()