from src.job_opening import HeadHunterAPI
from unittest.mock import patch
import pytest

@patch("requests.get")
def test_job_opening(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'items': [
        {'id': '111325640', 'premium': False, 'name': 'Менеджер по продажам', 'department': None, 'has_test': False}]}
    result = HeadHunterAPI()
    assert result.get_vacancies() == {'items': [
        {'id': '111325640', 'premium': False, 'name': 'Менеджер по продажам', 'department': None, 'has_test': False}]}
    mock_get.assert_called_once_with("https://api.hh.ru/vacancies", params={"text": None})



@patch("requests.get")
def test_job_opening_error(mock_get):
    mock_get.return_value.status_code = 400
    result = HeadHunterAPI()

    with pytest.raises(BaseException, match="Статус код: 400"):
        result.get_vacancies()

    mock_get.assert_called_once_with("https://api.hh.ru/vacancies", params={"text": None})