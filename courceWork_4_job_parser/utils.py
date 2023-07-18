import psycopg2 as psycopg2

from config import config

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

    return vacancies_all


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
                vac_title VARCHAR(255),
                vac_url VARCHAR(255),
                vac_payment INTEGER,
                vac_requirements TEXT,
                company_title VARCHAR(255)
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
                INSERT INTO vacancies (vac_title, vac_url, vac_payment, vac_requirements, company_title)
                    VALUES (%s, %s, %s, %s, %s)
                """,
                        (i['name'], i['url'], i['payment'], i['requirements'], i['employer'])
                        )
    conn.commit()
    conn.close()




