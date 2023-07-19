from utils import get_api_vacancies, create_database, save_data_to_database
from dbmanager import DBManager


def user_interaction():
    search_platforms = int(input("Введите платформу для поиска: 1 - HH, 2 - SJ, 3 - HH+SJ:   "))
    search_query = input("Введите слово для поиска в названии вакансии :   ")
    data = get_api_vacancies(search_platforms, search_query)
    create_database()
    save_data_to_database(data)

    while True:
        print(f"Перечень операций:\n"
              f"1 - получить список всех компаний и количество вакансий у каждой компании\n"
              f"2 - получить список всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию\n"
              f"3 - получить среднюю зарплату по вакансиям\n"
              f"4 - получить список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
              f"5 - получить список всех вакансий, в требованиях которых содержится искомое слово, например “python”\n"
              f"0 - ВЫХОД")
        num_operation = int(input('Введите номер операции:   '))

        if num_operation == 1:
            DBManager().get_companies_and_vacancies_count()
        elif num_operation == 2:
            DBManager().get_all_vacancies()
        elif num_operation == 3:
            print(f"{DBManager().get_avg_salary()} руб.")
        elif num_operation == 4:
            DBManager().get_vacancies_with_higher_salary()
        elif num_operation == 5:
            DBManager().get_vacancies_with_keyword()
        elif num_operation == 0:
            print('Пока!')
            break
        else:
            print("Нет такой операции. Попробуйте еще")
            continue


if __name__ == "__main__":
    user_interaction()
