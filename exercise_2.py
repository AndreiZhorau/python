def user_information(first_name=None, last_name=None, year_of_birth=None, residence=None, email=None,
                     phone_number=None):
    print(
        f'Имя: {first_name}. Фамилия: {last_name}. Год рождения: {year_of_birth}. Проживает в городе: {residence}. '
        f'Email: {email}. Номер телефона: {phone_number}')


user_information(first_name=input('Имя: '), last_name=input('Фамилия: '), year_of_birth=input('Год рождения: '),
                 residence=input('Проживает в городе: '), email=input('Email: '),
                 phone_number=input('Номер телефона: '))
