employees_dict = {}
unhappy_employees = []

with open('text_3.txt', 'r', encoding='utf-8') as employees:
    for line in employees:
        key, value = line.split()
        value = float(value)
        employees_dict[key] = value
        if value < 20000:
            unhappy_employees.append(key)

print(f'Список сотрудников с доходом меньше 20000: {unhappy_employees}.')
print(f'Средний доход сотрудников: {sum(employees_dict.values()) / len(employees_dict.values())}.')
