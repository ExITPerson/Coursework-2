
import os
import json


from src.file_saver import JsonSaver


def test_save_json_new_file(tmp_path):
    data = [{"id": 1, "name": "Test"}]
    test1 = JsonSaver
    test1.path = str(tmp_path)
    test1.save_data(data, "test")
    file_path = tmp_path / "test.json"

    assert os.path.exists(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        saved_data = json.load(f)
        assert saved_data == data


def test_update_save_data(tmp_path):
    test2 = JsonSaver
    test2.path = str(tmp_path)
    initial_data = [{'id': 1, 'name': 'Test'}]
    test2.save_data(initial_data, 'test')

    new_data = [{'id': 1, 'name': 'Updated'}, {'id': 2, 'name': 'New'}]
    test2.save_data(new_data, 'test')
    file_path = tmp_path / "test.json"

    with open(file_path, 'r', encoding='utf-8') as f:
        saved_data = json.load(f)
        expected_data = [{'id': 1, 'name': 'Updated'}, {'id': 2, 'name': 'New'}]
        assert saved_data == expected_data


def test_del_data(tmp_path):
    test3 = JsonSaver
    test3.path = tmp_path
    data = [{'id': 1, 'name': 'Test'}, {'id': 2, 'name': 'Another'}]
    test3.save_data(data, "test")

    data_to_del = [{'id': 1, 'name': 'Test'}]
    test3.del_data(data_to_del, "test")
    file_path = tmp_path / "test.json"

    with open(file_path, "r", encoding="utf-8") as f:
        saved_data = json.load(f)
        assert saved_data == [{'id': 2, 'name': 'Another'}]
        
def test_del_data_non_file(capsys):
    data = [{'id': 2, 'name': 'Another'}]
    JsonSaver.del_data(data, "non_file")
    result = capsys.readouterr()
    assert result.out.strip() == "Такого файла не существует"