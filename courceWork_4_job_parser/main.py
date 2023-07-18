from utils import get_api_vacancies, create_database, save_data_to_database


def user_interaction():
    search_platforms = int(input("Введите платформу для поиска: 1 - HH, 2 - SJ, 3 - HH+SJ:   "))
    search_query = input("Введите поисковый запрос:   ")
    data = get_api_vacancies(search_platforms, search_query)
    create_database()
    save_data_to_database(data)


if __name__ == "__main__":
    user_interaction()
