my_list = []

my_list.append(1)
my_list.append(1.1)
my_list.append(complex(1, 2))
my_list.append('string')
my_list.append(list('list'))
my_list.append(tuple('tuple'))
my_list.append(set('set'))
my_list.append(frozenset('frozenset'))
my_list.append(dict(key_1='val_1'))
my_list.append(False)
my_list.append(None)

print(f'Дан список: {my_list}')
for i in my_list:
    print(f'Типом данных переменной {i}, с позицией {my_list.index(i)}, является {type(i)}')
