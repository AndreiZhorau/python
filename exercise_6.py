products = []
analytics = {'название': [], 'цена': [], 'количество': [], 'ед.': []}
user_choice_check = True
i = 1

while user_choice_check:
    user_choice = (input('Вы хотите добавить товар? (yes / no): ')).lower()
    if user_choice == 'no':
        user_choice_check = False
    elif user_choice == 'yes':
        user_title = input(f'Введите название торава №{i}: ')
        analytics.get('название').append(user_title)
        user_price = int(input(f'Введите цену товара №{i}, руб.: '))
        analytics.get('цена').append(user_price)
        user_measure = input(f'Введите единицу измерения товара №{i} (кг, шт, и т.д.): ')
        if user_measure not in analytics.get('ед.'):
            analytics.get('ед.').append(user_measure)
        user_quantity = int(input(f'Введите количество товара №{i}, {user_measure}: '))
        analytics.get('количество').append(user_quantity)

        product = {'название': user_title, 'цена': user_price, 'количество': user_quantity, 'ед.': user_measure}
        products.append((i, product))
        i += 1
    else:
        print('Принимаются только ответы в форме yes / no.')
print(products)
print(analytics)
