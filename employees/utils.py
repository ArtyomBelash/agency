import random
from .models import Employee
from mimesis import Locale
from mimesis.enums import Gender
from mimesis import Generic


def create_employee():
    generic = Generic(locale=Locale.RU)
    genders = [Gender.MALE, Gender.FEMALE]
    positions = ['Manager', 'Senior Developer', 'Developer', 'Junior Developer']
    employees = []
    ceo = Employee(
        full_name=generic.person.full_name(random.choice(genders)),
        position='CEO',
        hire_date=generic.person.birthdate(min_year=1980, max_year=2001),
        salary=random.uniform(10000.00, 20000.00),
        manager=None
    )
    ceo.save()
    employees.append(ceo)

    for _ in range(999):
        full_name = generic.person.full_name(random.choice(genders))
        position = random.choice(positions)
        hire_date = generic.person.birthdate(min_year=1980, max_year=2001)
        salary = random.uniform(500.00, 9000.00)
        manager = random.choice(employees)
        employee = Employee(full_name=full_name, position=position, hire_date=hire_date, manager=manager, salary=salary)
        employee.save()
        employees.append(employee)
    print('Employees created!')


def delete_employee():
    for i in range(1, 1001):
        employee = Employee.objects.get(pk=i)
        employee.delete()
    print('Employees deleted!')
