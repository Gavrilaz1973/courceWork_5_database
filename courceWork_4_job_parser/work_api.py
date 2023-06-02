from abc import ABC, abstractmethod
import requests


class WorkAPI(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(WorkAPI):
    def get_vacancies(self, value):
        name_value = "name:" + value
        params = {'text': name_value, 'area': 1806, 'page': 0, 'per_page': 20}
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        return data


class SuperJobAPI(WorkAPI):
    def get_vacancies(self, value):
        url_str = 'https://api.superjob.ru/2.0/vacancies/?keyword=' + value + '&t=4&count=10/'
        req = requests.get(url_str, headers={"X-Api-App-Id": 'v3.h.4477191.ea224050553495a2c26261e15456f197766a658a.f1ecc74a69c175b80b0f99b2b057e8e87a0767b2'})
        data = req.content.decode()
        req.close()
        return data


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    print(hh_api.get_vacancies("Python"))
    superjob_api = SuperJobAPI()
    print(superjob_api.get_vacancies("Python"))