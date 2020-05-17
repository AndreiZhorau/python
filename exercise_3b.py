user_input = int(input('Введите номер месяца от 1 до 12: '))

if user_input < 1 or user_input > 12:
    print('От 1 до 12!')
else:
    months = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август',
              9: 'сентябрь',
              10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
    seasons = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}

    print(f'Это месяц {months[user_input]}, а сезон - {seasons[user_input // 3]}')
