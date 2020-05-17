user_input = int(input('Введите номер месяца от 1 до 12: '))

if user_input < 1 or user_input > 12:
    print('От 1 до 12!')
else:
    if user_input == 12:
        user_input = 0
    months_and_seasons = [
        ['декабрь', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
         'ноябрь'], ['зима', 'весна', 'лето', 'осень']]

    print(f'Это месяц {months_and_seasons[0][user_input]}, а сезон - {months_and_seasons[1][user_input // 3]}')
