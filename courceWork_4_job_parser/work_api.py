from abc import ABC, abstractmethod
import requests
import json


class WorkAPI(ABC):
    def __init__(self, text: str, count: int):
        self.text = text
        self.count = count

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def vacancies_for_user(self):
        pass


class HeadHunterAPI(WorkAPI):
    def get_vacancies(self):
        """Получаеет вакансии с сайта по ключевому слову и указаному количеству"""
        name_value = "name:" + self.text
        params = {'text': name_value, 'area': 1, 'page': 0, 'per_page': self.count}
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = json.loads(req.content.decode())
        req.close()
        return data

    def vacancies_for_user(self):
        """Преобразовавает полученные данные в список словарей с определенными полями"""
        vacancies_HH = []
        data = self.get_vacancies()
        for i in data['items']:
            if i['salary']:
                if i['salary']['from']:
                    vacancies_HH.append(dict(name=i['name'], url=i['alternate_url'], payment=i['salary']['from'],
                                       requirements=i['snippet']['requirement'], employer=i['employer']['name']))
                else:
                    vacancies_HH.append(dict(name=i['name'], url=i['alternate_url'], payment=0,
                                             requirements=i['snippet']['requirement'], employer=i['employer']['name']))
            else:
                vacancies_HH.append(dict(name=i['name'], url=i['alternate_url'], payment=0,
                                       requirements=i['snippet']['requirement'], employer=i['employer']['name']))
        return vacancies_HH


class SuperJobAPI(WorkAPI):
    def get_vacancies(self):
        url_str = f'https://api.superjob.ru/2.0/vacancies/?keyword={self.text}&t=4&count={self.count}/'
        req = requests.get(url_str, headers={"X-Api-App-Id": 'v3.h.4477191.ea224050553495a2c26261e15456f197766a658a.f1ecc74a69c175b80b0f99b2b057e8e87a0767b2'})
        data = json.loads(req.content.decode())
        req.close()
        return data

    def vacancies_for_user(self):
        vacancies_SJ = []
        data = self.get_vacancies()
        for i in data['objects']:
            vacancies_SJ.append(dict(name=i['profession'], url=i['link'], payment=i['payment_from'],
                                       requirements=i['candidat'], employer=i['firm_name']))
        return vacancies_SJ


