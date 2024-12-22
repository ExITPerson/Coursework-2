import pandas as pd
import json
import os.path

import pandas.errors

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
                    if content_id(data_file, x["id"]):
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
        if os.path.exists(f"data/{cls.file_name}.json"):
            with open(f"data/{cls.file_name}.json", "r", encoding="utf-8") as f:
                data_file = json.load(f)
            for x in data:
                if content_id(data_file, x["id"]):
                    del data_file[data_file.index(x)]
            with open(f"data/{cls.file_name}.json", "w", encoding="utf-8") as file:
                json.dump(data_file, file, indent=4, ensure_ascii=False)
        else:
            print("Такого файла не существует")

class CSVSaver(AbstractSaveFile):

    file_name = None

    @classmethod
    def save_data(cls, data, name):
        cls.file_name = name
        if os.path.exists(f"data/{cls.file_name}.csv"):
            csv_file = f"data/{cls.file_name}.csv"
            try:
                df = pd.read_csv(csv_file)
                data_file = df.to_dict("records")

                new_data = []
                for x in data:
                    if content_id(data_file, x["id"]):
                        new_data.append(x)
                for i in data:
                    new_data.append(i)
                print(len(new_data))
                df = pd.DataFrame(new_data)
                df.to_csv(f"data/{cls.file_name}.csv", index=False, encoding="utf-8")
            except pandas.errors.EmptyDataError:
                df = pd.DataFrame(data)
                df.to_csv(f"data/{cls.file_name}.csv", index=False, encoding="utf-8")
        else:
            df = pd.DataFrame(data)
            df.to_csv(f"data/{cls.file_name}.csv", index=False, encoding="utf-8")


    @classmethod
    def del_data(cls, data, name):
        cls.file_name = name
        if os.path.exists(f"data/{cls.file_name}.csv"):
            csv_file = f"data/{cls.file_name}.csv"
            try:
                df = pd.read_csv(csv_file)
                data_file = df.to_dict("records")
                new_data = []
                for x in data:
                    if content_id(data_file, x["id"]):
                        new_data.append(x)
                print(data_file)
                df = pd.DataFrame(new_data)
                df.to_csv(f"data/{cls.file_name}.csv", index=False, encoding="utf-8")
            except pandas.errors.EmptyDataError:
                print("Файл пустой, удалять нечего!")
        else:
            print("Такого файла не существует")


class ExcelSaver(AbstractSaveFile):

    file_name = None

    @classmethod
    def save_data(cls, data, name):
        cls.file_name = name
        if os.path.exists(f"data/{cls.file_name}.xlsx"):
            csv_file = f"data/{cls.file_name}.xlsx"

            df = pd.read_excel(csv_file)
            data_file = df.to_dict("records")
            new_data = []
            for x in data:
                if content_id(data_file, x["id"]):
                    new_data.append(x)
            for i in data:
                new_data.append(i)
            df = pd.DataFrame(new_data)
            df.to_excel(f"data/{cls.file_name}.xlsx", index=False)
        else:
            df = pd.DataFrame(data)
            df.to_excel(f"data/{cls.file_name}.xlsx", index=False)

    @classmethod
    def del_data(cls, data, name):
        cls.file_name = name
        if os.path.exists(f"data/{cls.file_name}.xlsx"):
            csv_file = f"data/{cls.file_name}.xlsx"

            df = pd.read_excel(csv_file)
            data_file = df.to_dict("records")
            new_data = []
            for x in data:
                if content_id(data_file, x["id"]):
                    new_data.append(x)
            df = pd.DataFrame(new_data)
            df.to_excel(f"data/{cls.file_name}.xlsx", index=False)

        else:
            print("Такого файла не существует")


class TXTSaver(AbstractSaveFile):

    file_name = None

    @classmethod
    def save_data(cls, data, name):
        cls.file_name = name
        if os.path.exists(f"data/{name}.txt"):
            with open(f"data/{cls.file_name}.txt", "r", encoding="utf-8") as f:
                data_file = json.load(f)
                for x in data:
                    if content_id(data_file, x["id"]):
                        del data_file[data_file.index(x)]
            for i in data:
                data_file.append(i)
            with open(f"data/{cls.file_name}.txt", "w", encoding="utf-8") as file:
                json.dump(data_file, file, indent=4, ensure_ascii=False)
        else:
            with open(f"data/{cls.file_name}.txt", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

    @classmethod
    def del_data(cls, data, name):
        cls.file_name = name
        if os.path.exists(f"data/{cls.file_name}.txt"):
            with open(f"data/{cls.file_name}.txt", "r", encoding="utf-8") as f:
                data_file = json.load(f)
            for x in data:
                if content_id(data_file, x["id"]):
                    del data_file[data_file.index(x)]
            with open(f"data/{cls.file_name}.txt", "w", encoding="utf-8") as file:
                json.dump(data_file, file, indent=4, ensure_ascii=False)
        else:
            print("Такого файла не существует")