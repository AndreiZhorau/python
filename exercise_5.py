def input_str_sum(user_input):
    input_sum = 0
    for i in user_input.split():
        if i.lower() == 'q':
            break
        else:
            input_sum += int(i)
    return input_sum


total = 0
continue_program = True

while continue_program:
    user_input = input('Введите числа разделенные пробелом. Для выхода введите "q": ')
    calculation = input_str_sum(user_input)
    if user_input.count('q') > 0 or user_input.count('Q') > 0:
        continue_program = False
    total += calculation
    print(f'Сумма чисел: {total}')
