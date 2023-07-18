--создание таблицы
CREATE TABLE vacancies(
                vac_id SERIAL PRIMARY KEY,
                vac_title VARCHAR(255),
                vac_url VARCHAR(255),
                vac_payment INTEGER,
                vac_requirements TEXT,
                company_title VARCHAR(255)
                )

--заполнение таблицы
INSERT INTO vacancies (vac_title, vac_url, vac_payment, vac_requirements, company_title)
VALUES (%s, %s, %s, %s, %s)

--Получает список всех компаний и количество вакансий у каждой компании
SELECT company_title, COUNT(*)
FROM vacancies
GROUP BY company_title

--Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
SELECT company_title, vac_title, vac_payment, vac_url
FROM vacancies

--Получает среднюю зарплату по вакансиям
SELECT AVG(vac_payment)
FROM vacancies

--олучает список всех вакансий, у которых зарплата выше средней по всем вакансиям
SELECT * FROM vacancies WHERE vac_payment > {self.get_avg_salary()}

--Получает список всех вакансий, в требованиях которых содержатся переданные в метод слова
SELECT * FROM vacancies WHERE vac_requirements LIKE '%{search_word}%'