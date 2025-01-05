from unittest.mock import Mock, patch

import pytest

from src.job_opening import HeadHunterAPI


@patch("requests.get")
def test_get_response(mock_get: Mock) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"key": "value"}

    api = HeadHunterAPI()

    response = api._HeadHunterAPI__get_response()
    assert response == {"key": "value"}


@patch("requests.get")
def test_get_response_error(mock_get: Mock) -> None:
    mock_get.return_value.status_code = 404

    api = HeadHunterAPI()

    with pytest.raises(BaseException, match="Статус код: 404"):
        api._HeadHunterAPI__get_response()


@patch("requests.get")
def test_job_opening(mock_get: Mock) -> None:
    mock_get.side_effect = [
        Mock(
            status_code=200,
            json=lambda: {
                "pages": 1,
                "items": [
                    {
                        "id": "111325640",
                        "premium": False,
                        "name": "Менеджер по продажам",
                        "department": None,
                        "has_test": False,
                    }
                ],
            },
        ),
    ]
    result = HeadHunterAPI().get_vacancies("Менеджер")

    assert len(result) == 1
    assert result == [
        {"id": "111325640", "premium": False, "name": "Менеджер по продажам", "department": None, "has_test": False}
    ]

    mock_get.assert_called()
    mock_get.assert_any_call(
        "https://api.hh.ru/vacancies",
        headers={"User-Agent": "HH-User-Agent"},
        params={"text": "Менеджер", "page": 1, "per_page": 100},
    )


@patch("requests.get")
def test_job_opening_error(mock_get: Mock) -> None:
    mock_get.return_value.status_code = 400
    result = HeadHunterAPI()

    with pytest.raises(BaseException, match="Статус код: 400"):
        result.get_vacancies("Менеджер")

    mock_get.assert_called_once_with(
        "https://api.hh.ru/vacancies",
        headers={"User-Agent": "HH-User-Agent"},
        params={"text": "Менеджер", "page": 0, "per_page": 100},
    )
