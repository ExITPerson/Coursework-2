from src.job_opening import HeadHunterAPI
from unittest.mock import patch, Mock
import pytest


@patch("requests.get")
def test_job_opening(mock_get):
    mock_get.side_effect = [Mock(status_code = 200, json = lambda: {"pages": 1}),
                            Mock(status_code=200, json=lambda: {"items": [
        {'id': '111325640', 'premium': False, 'name': 'Менеджер по продажам', 'department': None, 'has_test': False}
                            ]})]
    result = HeadHunterAPI("Менеджер").get_vacancies()


    assert  len(result) == 1
    assert result == [{'id': '111325640', 'premium': False, 'name': 'Менеджер по продажам', 'department': None, 'has_test': False}]

    mock_get.assert_called()
    mock_get.assert_any_call("https://api.hh.ru/vacancies", headers={'User-Agent': 'HH-User-Agent'}, params={"text": "Менеджер", 'page': 1, 'per_page': 100})



@patch("requests.get")
def test_job_opening_error(mock_get):
    mock_get.return_value.status_code = 400
    result = HeadHunterAPI("Менеджер")

    with pytest.raises(BaseException, match="Статус код: 400"):
        result.get_vacancies()

    mock_get.assert_called_once_with("https://api.hh.ru/vacancies", headers={'User-Agent': 'HH-User-Agent'}, params={'text': 'Менеджер', 'page': 0, 'per_page': 100})