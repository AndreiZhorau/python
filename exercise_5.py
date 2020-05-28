with open('text_5.txt', 'w+', encoding='utf-8') as local_file:
    local_file.write(input('Введите числа разделенные пробелом: '))
    local_file.seek(0)
    try:
        numbers_list = [float(i) for i in local_file.readline().split()]
        print(f'Сумма чисел: {sum(numbers_list)}')
    except ValueError:
        print('Только числа!')
