from work_api import SuperJobAPI, HeadHunterAPI


class Vacancies:
    all = []

    def __init__(self, name, url, payment, requirements):
        self.name = name
        self.url = url
        self.payment = payment
        self.requirements = requirements
        Vacancies.all.append(self)

    def __str__(self):
        return f"\nДолжность: {self.name}\nСсылка: {self.url}\nЗарплата: {self.payment}\nТребования: {self.requirements}\n"

    def __lt__(self, other):
        if isinstance(other, Vacancies):
            return self.payment < other.payment
        else:
            raise TypeError("other is not Vacancies")
