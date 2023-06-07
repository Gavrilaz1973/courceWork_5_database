import json
from abc import ABC, abstractmethod


class FileSaver(ABC):
    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def get_vacancies_of_file(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(FileSaver):

    def add_vacancy(self, data):
        with open('vacancies_all.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def get_vacancies_of_file(self):
        with open('vacancies_all.json', 'r', encoding='utf-8') as f:
            file_data = json.load(f)
        return file_data

    def delete_vacancy(self):
        pass




