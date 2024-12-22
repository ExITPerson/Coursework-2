import json
import os.path

from src.abstract_classes import AbstractSaveFile
from src.utils import content_id


class JsonSaver(AbstractSaveFile):

    def save_data(self, data, file_name):
        if os.path.exists(f"data/{file_name}.json"):
            with open(f"data/{file_name}.json", "r", encoding="utf-8") as f:
                data_file = json.load(f)
                for x in data_file:
                    if content_id(file_name, x["id"]):
                        del data_file[data_file.index(x)]
                for i in data:
                    data_file.append(i)
            with open(f"data/{file_name}.json", "w", encoding="utf-8") as file:
                json.dump(data_file, file, indent=4, ensure_ascii=False)
        else:
            with open(f"data/{file_name}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)




    def del_data(self, data, name_file):
        pass