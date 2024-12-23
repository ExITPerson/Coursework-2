import json
import os.path

import pandas as pd
import pandas.errors

from src.abstract_classes import AbstractSaveFile


class JsonSaver(AbstractSaveFile):

    file_name = None
    path = "data"

    @classmethod
    def save_data(cls, data: list, name: str) -> None:
        cls.file_name = name
        if os.path.exists(f"{cls.path}/{name}.json"):
            with open(f"{cls.path}/{cls.file_name}.json", "r", encoding="utf-8") as f:
                data_file = json.load(f)

            data_file = [item for item in data_file if item["id"] not in {x["id"] for x in data}]
            data_file.extend(data)

            with open(f"{cls.path}/{cls.file_name}.json", "w", encoding="utf-8") as file:
                json.dump(data_file, file, indent=4, ensure_ascii=False)
        else:
            with open(f"{cls.path}/{cls.file_name}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

    @classmethod
    def del_data(cls, data: list, name: str) -> None:
        cls.file_name = name
        if os.path.exists(f"{cls.path}/{cls.file_name}.json"):
            with open(f"{cls.path}/{cls.file_name}.json", "r", encoding="utf-8") as f:
                data_file = json.load(f)

            data_file = [item for item in data_file if item["id"] not in {x["id"] for x in data}]

            with open(f"{cls.path}/{cls.file_name}.json", "w", encoding="utf-8") as file:
                json.dump(data_file, file, indent=4, ensure_ascii=False)
        else:
            print("Такого файла не существует")


class CSVSaver(AbstractSaveFile):

    path = "data"
    file_name = None

    @classmethod
    def save_data(cls, data: list, name: str) -> None:
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
    def del_data(cls, data: list, name: str) -> None:
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


class ExcelSaver(AbstractSaveFile):

    path = "data"
    file_name = None

    @classmethod
    def save_data(cls, data: list, name: str) -> None:
        cls.file_name = name
        if os.path.exists(f"{cls.path}/{cls.file_name}.xlsx"):
            csv_file = f"{cls.path}/{cls.file_name}.xlsx"
            df = pd.read_excel(csv_file)
            data_file = df.to_dict("records")

            new_data = [item for item in data_file if item["id"] not in {x["id"] for x in data}]
            new_data.extend(data)

            df = pd.DataFrame(new_data)
            df.to_excel(f"{cls.path}/{cls.file_name}.xlsx", index=False)
        else:
            df = pd.DataFrame(data)
            df.to_excel(f"{cls.path}/{cls.file_name}.xlsx", index=False)

    @classmethod
    def del_data(cls, data: list, name: str) -> None:
        cls.file_name = name
        if os.path.exists(f"{cls.path}/{cls.file_name}.xlsx"):
            csv_file = f"{cls.path}/{cls.file_name}.xlsx"

            df = pd.read_excel(csv_file)
            data_file = df.to_dict("records")

            new_data = [item for item in data_file if item["id"] not in {x["id"] for x in data}]

            df = pd.DataFrame(new_data)
            df.to_excel(f"{cls.path}/{cls.file_name}.xlsx", index=False)

        else:
            print("Такого файла не существует")


class TXTSaver(AbstractSaveFile):
    path = "data"

    file_name = None

    @classmethod
    def save_data(cls, data: list, name: str) -> None:
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
    def del_data(cls, data: list, name: str) -> None:
        cls.file_name = name
        if os.path.exists(f"{cls.path}/{cls.file_name}.txt"):
            with open(f"{cls.path}/{cls.file_name}.txt", "r", encoding="utf-8") as f:
                data_file = json.load(f)

            data_file = [item for item in data_file if item["id"] not in {x["id"] for x in data}]

            with open(f"{cls.path}/{cls.file_name}.txt", "w", encoding="utf-8") as file:
                json.dump(data_file, file, indent=4, ensure_ascii=False)
        else:
            print("Такого файла не существует")
