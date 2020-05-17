my_list = [7, 5, 3, 3, 3, 2]

new_number = int(input('Введите новый элемент рейтинга: '))

if my_list[-1] >= new_number:
    my_list.append(new_number)
else:
    for i in range(0, len(my_list)):
        if my_list[i] < new_number:
            my_list.insert(i, new_number)
            break

print(my_list)
