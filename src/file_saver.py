import json
import os.path

from src.abstract_classes import AbstractSaveFile
from src.utils import content_id


class JsonSaver(AbstractSaveFile):

    file_name = None

    @classmethod
    def save_data(cls, data, name):
        cls.file_name = name
        if os.path.exists(f"data/{name}.json"):
            with open(f"data/{cls.file_name}.json", "r", encoding="utf-8") as f:
                data_file = json.load(f)
                for x in data:
                    if content_id(cls.file_name, x["id"]):
                        del data_file[data_file.index(x)]
            for i in data:
                data_file.append(i)
            with open(f"data/{cls.file_name}.json", "w", encoding="utf-8") as file:
                json.dump(data_file, file, indent=4, ensure_ascii=False)
        else:
            with open(f"data/{cls.file_name}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

    @classmethod
    def del_data(cls, data, name):
        cls.file_name = name
        with open(f"data/{cls.file_name}.json", "r", encoding="utf-8") as f:
            data_file = json.load(f)
        for x in data:
            if content_id(cls.file_name, x["id"]):
                del data_file[data_file.index(x)]
        with open(f"data/{cls.file_name}.json", "w", encoding="utf-8") as file:
            json.dump(data_file, file, indent=4, ensure_ascii=False)