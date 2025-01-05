import json
import os.path

import pandas as pd
import pandas.errors

from typing import Any
from src.abstract_classes import AbstractSaveFile


class JsonSaver(AbstractSaveFile):
    """Класс для сохранения файла в формате json"""

    __file_name = "new_file"
    path = "data"

    @classmethod
    def save_data(cls, data: list, name: str = None) -> None:
        """Функция сохранения и добавления данных в файл"""
        if len(name) > 0:
            cls.__file_name = name
        if os.path.exists(f"{cls.path}/{cls.__file_name}.json"):
            with open(f"{cls.path}/{cls.__file_name}.json", "r", encoding="utf-8") as f:
                data_file = json.load(f)

            data_file = [item for item in data_file if item["id"] not in {x["id"] for x in data}]
            data_file.extend(data)

            with open(f"{cls.path}/{cls.__file_name}.json", "w", encoding="utf-8") as file:
                json.dump(data_file, file, indent=4, ensure_ascii=False)
        else:
            with open(f"{cls.path}/{cls.__file_name}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

    @classmethod
    def del_data(cls, data: list, name: str = None) -> None:
        """Функция для удаления данных из файла"""
        if len(name) > 0:
            cls.__file_name = name
        if os.path.exists(f"{cls.path}/{cls.__file_name}.json"):
            with open(f"{cls.path}/{cls.__file_name}.json", "r", encoding="utf-8") as f:
                data_file = json.load(f)

            data_file = [item for item in data_file if item["id"] not in {x["id"] for x in data}]

            with open(f"{cls.path}/{cls.__file_name}.json", "w", encoding="utf-8") as file:
                json.dump(data_file, file, indent=4, ensure_ascii=False)
        else:
            print("Такого файла не существует")

    @staticmethod
    def get_data(path: str, file_name: str) -> Any:
        if os.path.exists(f"{path}/{file_name}.json"):
            with open(f"{path}/{file_name}.json", "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            print("Такого файла не существует.")


class CSVSaver(AbstractSaveFile):
    """Класс для сохранения файла в формате csv"""

    path = "data"
    file_name = "new_file"

    @classmethod
    def save_data(cls, data: list, name: str = None) -> None:
        """Функция сохранения и добавления данных в файл"""
        if len(name) > 0:
            cls.file_name = name
        if os.path.exists(f"{cls.path}/{cls.file_name}.csv"):
            csv_file = f"{cls.path}/{cls.file_name}.csv"
            try:
                df = pd.read_csv(csv_file)
                data_file = df.to_dict("records")

                new_data = [item for item in data_file if item["id"] not in {x["id"] for x in data}]
                new_data.extend(data)

                df = pd.DataFrame(new_data)
                df.to_csv(f"{cls.path}/{cls.file_name}.csv", index=False, encoding="utf-8")

            except pandas.errors.EmptyDataError:
                df = pd.DataFrame(data)
                df.to_csv(f"{cls.path}/{cls.file_name}.csv", index=False, encoding="utf-8")
        else:
            df = pd.DataFrame(data)
            df.to_csv(f"{cls.path}/{cls.file_name}.csv", index=False, encoding="utf-8")

    @classmethod
    def del_data(cls, data: list, name: str = None) -> None:
        """Функция для удаления данных из файла"""
        if len(name) > 0:
            cls.file_name = name
        if os.path.exists(f"{cls.path}/{cls.file_name}.csv"):
            csv_file = f"{cls.path}/{cls.file_name}.csv"
            try:
                df = pd.read_csv(csv_file)
                data_file = df.to_dict("records")

                new_data = [item for item in data_file if item["id"] not in {x["id"] for x in data}]

                df = pd.DataFrame(new_data)
                df.to_csv(f"{cls.path}/{cls.file_name}.csv", index=False, encoding="utf-8")
            except pandas.errors.EmptyDataError:
                print("Файл пустой, удалять нечего!")
        else:
            print("Такого файла не существует")

    @staticmethod
    def get_data(path: str, file_name: str) -> Any:
        if os.path.exists(f"{path}/{file_name}.csv"):
            csv_file = f"{path}/{file_name}.csv"
            df = pd.read_csv(csv_file)
            data_file = df.to_dict("records")
            return data_file
        else:
            print("Такого файла не существует.")


class ExcelSaver(AbstractSaveFile):
    """Класс для сохранения файла в формате xlsx"""

    path = "data"
    file_name = "new_file"

    @classmethod
    def save_data(cls, data: list, name: str = None) -> None:
        """Функция сохранения и добавления данных в файл"""
        if len(name) > 0:
            cls.file_name = name
        if os.path.exists(f"{cls.path}/{cls.file_name}.xlsx"):
            excel_file = f"{cls.path}/{cls.file_name}.xlsx"
            df = pd.read_excel(excel_file)
            data_file = df.to_dict("records")

            new_data = [item for item in data_file if item["id"] not in {x["id"] for x in data}]
            new_data.extend(data)

            df = pd.DataFrame(new_data)
            df.to_excel(f"{cls.path}/{cls.file_name}.xlsx", index=False)
        else:
            df = pd.DataFrame(data)
            df.to_excel(f"{cls.path}/{cls.file_name}.xlsx", index=False)

    @classmethod
    def del_data(cls, data: list, name: str = None) -> None:
        """Функция для удаления данных из файла"""
        if len(name) > 0:
            cls.file_name = name
        if os.path.exists(f"{cls.path}/{cls.file_name}.xlsx"):
            excel_file = f"{cls.path}/{cls.file_name}.xlsx"

            df = pd.read_excel(excel_file)
            data_file = df.to_dict("records")

            new_data = [item for item in data_file if item["id"] not in {x["id"] for x in data}]

            df = pd.DataFrame(new_data)
            df.to_excel(f"{cls.path}/{cls.file_name}.xlsx", index=False)

        else:
            print("Такого файла не существует")

    @staticmethod
    def get_data(path: str, file_name: str) -> Any:
        if os.path.exists(f"{path}/{file_name}.xlsx"):
            excel_file = f"{path}/{file_name}.xlsx"
            df = pd.read_excel(excel_file)
            data_file = df.to_dict("records")
            return data_file
        else:
            print("Такого файла не существует.")


class TXTSaver(AbstractSaveFile):
    """Класс для сохранения файла в формате txt"""

    path = "data"
    file_name = "new_file"

    @classmethod
    def save_data(cls, data: list, name: str = None) -> None:
        """Функция сохранения и добавления данных в файл"""
        if len(name) > 0:
            cls.file_name = name
        if os.path.exists(f"{cls.path}/{name}.txt"):
            with open(f"{cls.path}/{cls.file_name}.txt", "r", encoding="utf-8") as f:
                data_file = json.load(f)

            data_file = [item for item in data_file if item["id"] not in {x["id"] for x in data}]
            data_file.extend(data)

            with open(f"{cls.path}/{cls.file_name}.txt", "w", encoding="utf-8") as file:
                json.dump(data_file, file, indent=4, ensure_ascii=False)
        else:
            with open(f"{cls.path}/{cls.file_name}.txt", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

    @classmethod
    def del_data(cls, data: list, name: str = None) -> None:
        """Функция для удаления данных из файла"""
        if len(name) > 0:
            cls.file_name = name
        if os.path.exists(f"{cls.path}/{cls.file_name}.txt"):
            with open(f"{cls.path}/{cls.file_name}.txt", "r", encoding="utf-8") as f:
                data_file = json.load(f)

            data_file = [item for item in data_file if item["id"] not in {x["id"] for x in data}]

            with open(f"{cls.path}/{cls.file_name}.txt", "w", encoding="utf-8") as file:
                json.dump(data_file, file, indent=4, ensure_ascii=False)
        else:
            print("Такого файла не существует")

    @staticmethod
    def get_data(path: str, file_name: str) -> Any:
        if os.path.exists(f"{path}/{file_name}.txt"):
            with open(f"{path}/{file_name}.txt", "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            print("Такого файла не существует.")
