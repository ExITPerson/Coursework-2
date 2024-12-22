from src.file_saver import JsonSaver, CSVSaver, ExcelSaver, TXTSaver
from src.job_opening import HeadHunterAPI
import json

from src.vacancy import Vacancy

if __name__ == "__main__":
    hh_vacancies = HeadHunterAPI("Python").get_vacancies()
    #print(hh_vacancies)

    job_search = Vacancy("100000-150000", "Москва", 4, ["sql", "junior"])
    vacancy = job_search.custom(hh_vacancies)

    vacancy1 = job_search.filter_vacancies()
    for vacancy in vacancy1:
        print(vacancy["id"])


    # data = JsonSaver()
    # data1 = data.save_data(vacancy1, "vacancies")
    # data2 = data.del_data(vacancy1, "vacancies")
    # data_csv = CSVSaver()
    # data2 = data_csv.save_data(vacancy1, "vacancies")
    # data_del = data_csv.del_data(vacancy1, "vacancies")
    # data_excel = ExcelSaver()
    # data_save = data_excel.save_data(vacancy1, "vacancies")
    # data_del = data_excel.del_data(vacancy1, "vacancies")
    # data = TXTSaver()
    # data_save = data.save_data(vacancy1, "vacancies")
    # data_del = data.del_data(vacancy1, "vacancies")



