

class Vacancies:
    def __init__(self, name, url, payment, requirements):
        self.name = name
        self.url = url
        self.payment = payment
        self.requirements = requirements

    def __str__(self):
        return f"Должность: {self.name}\nСсылка: {self.url}\nЗарплата: {self.payment}\nТребования: {self.requirements}"


vac = Vacancies('ssss', 'www jgjgj', '100000-150000 руб', 'не бухать')
print(vac)