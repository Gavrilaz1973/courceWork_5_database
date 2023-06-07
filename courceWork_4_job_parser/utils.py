from file_saver import JSONSaver
from vacancy import Vacancies
from work_api import HeadHunterAPI, SuperJobAPI


def get_api_vacancies(platform, word):
    count_vac = 5   # Количество вакансий с платформы

    if platform == 1:
        vacancies_all = HeadHunterAPI(word, count_vac).vacancies_for_user()
        print(f'Найдено {len(vacancies_all)} вакансий с платформы Head Hunter')
    elif platform == 2:
        vacancies_all = SuperJobAPI(word, count_vac).vacancies_for_user()
        print(f'Найдено {len(vacancies_all)} вакансий с платформы Super Job')
    elif platform == 3:
        vacancies_all = HeadHunterAPI(word, count_vac).vacancies_for_user() + SuperJobAPI(word, count_vac).vacancies_for_user()
        print(f'Найдено {len(vacancies_all)} вакансий с платформ Super Job и Head Hunter')
    else:
        print('Такой платформы нет, попробуйте снова')
        exit()

    JSONSaver().add_vacancy(vacancies_all)



def filter_vacancies(filter_words):
    # filter_salary = []
    # for vacancy in JSONSaver().get_vacancies_of_file():
    #     if filter_words(0) <= vacancy['payment'] <= filter_words(1):
    #         filter_salary.append(vacancy)
    # return filter_salary
    pass


def get_top_vacancies(top_n):
    n = 0
    for vacancy in JSONSaver().get_vacancies_of_file():
        Vacancies(vacancy['name'], vacancy['url'], vacancy['payment'], vacancy['requirements'])
    for i in sorted(Vacancies.all, reverse=True):
        print(i)
        n += 1
        if n == top_n:
            return



