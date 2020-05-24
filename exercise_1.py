from sys import argv


def salary(hours=160, rate=10, bonus=0):
    return hours * rate + bonus
    pass


try:
    name, user_hours, user_rate, user_bonus = argv
    print(
        f'Зарплата сотрудника составила: {salary(int(user_hours), int(user_rate), int(user_bonus))} орехов.'
        f'\nОтработано: {user_hours} часов. Ставка: {user_rate} орехов/час. Бонус: {user_bonus} орехов.')
except ValueError:
    print('Введено недостаточно или некорректные значения')

# учесть отсутствие значений и ввод строк try / except
