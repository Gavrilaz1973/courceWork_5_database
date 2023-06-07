from utils import get_api_vacancies, filter_vacancies, get_top_vacancies


def user_interaction():
    search_platforms = int(input("Введите платформу для поиска: 1 - HH, 2 - SJ, 3 - HH+SJ:   "))
    search_query = input("Введите поисковый запрос:   ")
    get_api_vacancies(search_platforms, search_query)

    top_n = int(input("Введите количество вакансий для вывода в топ N по начальной зарплате:   "))
    get_top_vacancies(top_n)

    filter_words = input("Введите ключевые слова для фильтрации вакансий:   ").split(', ')
    # filter_vacancies(filter_words)
    print(filter_words)

if __name__ == "__main__":
    user_interaction()
