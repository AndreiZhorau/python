my_func = lambda a, b, c: a + b + c - min(a, b, c)

test = my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')),
               int(input('Введите третье число: ')))
print(test)