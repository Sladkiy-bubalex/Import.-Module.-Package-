from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import date

if __name__ == '__main__':
    now = date.today()
    print(f'Год: {now.year} Месяц: {now.month} День: {now.day}')
    calculate_salary()
    get_employees()