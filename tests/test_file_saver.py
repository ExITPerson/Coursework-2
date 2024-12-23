import json
import os
from typing import Callable

import pandas as pd
from pytest import CaptureFixture

from src.file_saver import CSVSaver, ExcelSaver, JsonSaver, TXTSaver


def test_save_json_new_file(tmp_path: Callable) -> None:
    data = [{"id": 1, "name": "Test"}]
    test1 = JsonSaver
    test1.path = str(tmp_path)
    test1.save_data(data, "test")
    file_path = tmp_path / "test.json"

    assert os.path.exists(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        saved_data = json.load(f)
        assert saved_data == data


def test_update_save_data(tmp_path: Callable) -> None:
    test2 = JsonSaver
    test2.path = str(tmp_path)
    initial_data = [{"id": 1, "name": "Test"}]
    test2.save_data(initial_data, "test")

    new_data = [{"id": 1, "name": "Updated"}, {"id": 2, "name": "New"}]
    test2.save_data(new_data, "test")
    file_path = tmp_path / "test.json"

    with open(file_path, "r", encoding="utf-8") as f:
        saved_data = json.load(f)
        expected_data = [{"id": 1, "name": "Updated"}, {"id": 2, "name": "New"}]
        assert saved_data == expected_data


def test_del_data(tmp_path: Callable) -> None:
    test3 = JsonSaver
    test3.path = tmp_path
    data = [{"id": 1, "name": "Test"}, {"id": 2, "name": "Another"}]
    test3.save_data(data, "test")

    data_to_del = [{"id": 1, "name": "Test"}]
    test3.del_data(data_to_del, "test")
    file_path = tmp_path / "test.json"

    with open(file_path, "r", encoding="utf-8") as f:
        saved_data = json.load(f)
        assert saved_data == [{"id": 2, "name": "Another"}]


def test_del_data_non_file(capsys: CaptureFixture) -> None:
    data = [{"id": 2, "name": "Another"}]
    JsonSaver.del_data(data, "non_file")
    result = capsys.readouterr()
    assert result.out.strip() == "Такого файла не существует"


def test_save_json_new_file_txt(tmp_path: Callable) -> None:
    data = [{"id": 1, "name": "Test"}]
    test1 = TXTSaver
    test1.path = str(tmp_path)
    test1.save_data(data, "test")
    file_path = tmp_path / "test.txt"

    assert os.path.exists(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        saved_data = json.load(f)
        assert saved_data == data


def test_update_save_data_txt(tmp_path: Callable) -> None:
    test2 = TXTSaver
    test2.path = str(tmp_path)
    initial_data = [{"id": 1, "name": "Test"}]
    test2.save_data(initial_data, "test")

    new_data = [{"id": 1, "name": "Updated"}, {"id": 2, "name": "New"}]
    test2.save_data(new_data, "test")
    file_path = tmp_path / "test.txt"

    with open(file_path, "r", encoding="utf-8") as f:
        saved_data = json.load(f)
        expected_data = [{"id": 1, "name": "Updated"}, {"id": 2, "name": "New"}]
        assert saved_data == expected_data


def test_del_data_txt(tmp_path: Callable) -> None:
    test3 = TXTSaver
    test3.path = tmp_path
    data = [{"id": 1, "name": "Test"}, {"id": 2, "name": "Another"}]
    test3.save_data(data, "test")

    data_to_del = [{"id": 1, "name": "Test"}]
    test3.del_data(data_to_del, "test")
    file_path = tmp_path / "test.txt"

    with open(file_path, "r", encoding="utf-8") as f:
        saved_data = json.load(f)
        assert saved_data == [{"id": 2, "name": "Another"}]


def test_del_data_non_file_txt(capsys: CaptureFixture) -> None:
    data = [{"id": 2, "name": "Another"}]
    TXTSaver.del_data(data, "non_file")
    result = capsys.readouterr()
    assert result.out.strip() == "Такого файла не существует"


def test_update_save_data_xlsx(tmp_path: Callable) -> None:
    test2 = ExcelSaver
    test2.path = str(tmp_path)
    initial_data = [{"id": 1, "name": "Test"}]
    test2.save_data(initial_data, "test")

    new_data = [{"id": 1, "name": "Updated"}, {"id": 2, "name": "New"}]
    test2.save_data(new_data, "test")
    file_path = tmp_path / "test.xlsx"

    df = pd.read_excel(file_path)
    saved_data = df.to_dict("records")
    expected_data = [{"id": 1, "name": "Updated"}, {"id": 2, "name": "New"}]
    assert saved_data == expected_data


def test_del_data_xlsx(tmp_path: Callable) -> None:
    test3 = ExcelSaver
    test3.path = tmp_path
    data = [{"id": 1, "name": "Test"}, {"id": 2, "name": "Another"}]
    test3.save_data(data, "test")

    data_to_del = [{"id": 1, "name": "Test"}]
    test3.del_data(data_to_del, "test")
    file_path = tmp_path / "test.xlsx"

    df = pd.read_excel(file_path)
    saved_data = df.to_dict("records")
    assert saved_data == [{"id": 2, "name": "Another"}]


def test_del_data_non_file_xlsx(capsys: CaptureFixture) -> None:
    data = [{"id": 2, "name": "Another"}]
    ExcelSaver.del_data(data, "non_file")
    result = capsys.readouterr()
    assert result.out.strip() == "Такого файла не существует"


def test_save_json_new_file_xlsx(tmp_path: Callable) -> None:
    data = [{"id": 1, "name": "Test"}]
    test1 = ExcelSaver
    test1.path = str(tmp_path)
    test1.save_data(data, "test")
    file_path = tmp_path / "test.xlsx"

    assert os.path.exists(file_path)

    df = pd.read_excel(file_path)
    saved_data = df.to_dict("records")
    assert saved_data == data


def test_update_save_data_csv(tmp_path: Callable) -> None:
    test2 = CSVSaver
    test2.path = str(tmp_path)
    initial_data = [{"id": 1, "name": "Test"}]
    test2.save_data(initial_data, "test")

    new_data = [{"id": 1, "name": "Updated"}, {"id": 2, "name": "New"}]
    test2.save_data(new_data, "test")
    file_path = tmp_path / "test.csv"

    df = pd.read_csv(file_path)
    saved_data = df.to_dict("records")
    expected_data = [{"id": 1, "name": "Updated"}, {"id": 2, "name": "New"}]
    assert saved_data == expected_data


def test_del_data_csv(tmp_path: Callable) -> None:
    test3 = CSVSaver
    test3.path = tmp_path
    data = [{"id": 1, "name": "Test"}, {"id": 2, "name": "Another"}]
    test3.save_data(data, "test")

    data_to_del = [{"id": 1, "name": "Test"}]
    test3.del_data(data_to_del, "test")
    file_path = tmp_path / "test.csv"

    df = pd.read_csv(file_path)
    saved_data = df.to_dict("records")
    assert saved_data == [{"id": 2, "name": "Another"}]


def test_del_data_non_file_csv(capsys: CaptureFixture) -> None:
    data = [{"id": 2, "name": "Another"}]
    CSVSaver.del_data(data, "non_file")
    result = capsys.readouterr()
    assert result.out.strip() == "Такого файла не существует"


def test_save_json_new_file_csv(tmp_path: Callable) -> None:
    data = [{"id": 1, "name": "Test"}]
    test1 = CSVSaver
    test1.path = str(tmp_path)
    test1.save_data(data, "test")
    file_path = tmp_path / "test.csv"

    assert os.path.exists(file_path)

    df = pd.read_csv(file_path)
    saved_data = df.to_dict("records")
    assert saved_data == data
