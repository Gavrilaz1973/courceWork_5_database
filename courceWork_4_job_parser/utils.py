import psycopg2 as psycopg2

from config import config
from file_saver import JSONSaver
from vacancy import Vacancies
from work_api import HeadHunterAPI, SuperJobAPI


def get_api_vacancies(platform, word):
    count_vac = 100   # Количество вакансий с платформы

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

    # JSONSaver().add_vacancy(vacancies_all)
    return vacancies_all

def filter_vacancies(filter_words):
    filter_vac = []
    for vacancy in JSONSaver().get_vacancies_of_file():

        for i in filter_words:
            if str(i).lower() in str(vacancy['requirements']).lower():
                filter_vac.append(vacancy)
                break

    print(f'Найдено {len(filter_vac)} вакансий')
    count_show = input('Сколько показать?   ')
    n = 0
    for vacancy in filter_vac:
        n += 1
        print(Vacancies(vacancy['name'], vacancy['url'], vacancy['payment'], vacancy['requirements']))
        if n == count_show:
            return


def get_top_vacancies(top_n):
    n = 0
    for vacancy in JSONSaver().get_vacancies_of_file():
        Vacancies(vacancy['name'], vacancy['url'], vacancy['payment'], vacancy['requirements'])
    for i in sorted(Vacancies.all, reverse=True):
        print(i)
        n += 1
        if n == top_n:
            return


def create_database() -> None:
    """Создает новую базу данных."""
    db_name = 'db_curse_work_5'
    params = config()
    conn = None
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"DROP DATABASE {db_name}")
    cur.execute(f"CREATE DATABASE {db_name}")
    conn.close()

    conn = psycopg2.connect(dbname=db_name, **params)
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies(
                vac_id SERIAL PRIMARY KEY,
                Наименование VARCHAR(255),
                Ссылка VARCHAR(255),
                Зарплата INTEGER,
                Требования TEXT,
                Кампания VARCHAR(255)
                )
                """)
    conn.commit()
    conn.close()


def save_data_to_database(data):
    db_name = 'db_curse_work_5'
    params = config()
    conn = psycopg2.connect(dbname=db_name, **params)
    with conn.cursor() as cur:
        for i in data:
            cur.execute("""
                INSERT INTO vacancies (Наименование, Ссылка, Зарплата, Требования, Кампания)
                    VALUES (%s, %s, %s, %s, %s)
                """,
                        (i['name'], i['url'], i['payment'], i['requirements'], i['employer'])
                        )
    conn.commit()
    conn.close()




if __name__ == "__main__":
    create_database()

