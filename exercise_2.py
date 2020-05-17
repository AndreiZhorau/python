my_list = list(input('Все что вы введете будет преобразовано в список с обменом значений соседних элементов: '))

for i in range(1, len(my_list), 2):
    popped_variable = my_list.pop(i)
    my_list.insert(i - 1, popped_variable)

print(my_list)
