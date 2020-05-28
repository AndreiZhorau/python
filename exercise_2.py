with open('text_2.TXT', 'r', encoding='utf-8') as local_file:
    local_file_list = local_file.readlines()

print(f'Число строк: {len(local_file_list)}')
"""
Вариант подсчета слов через колличество пробелов + 1 
"""

string_counter = 1
for string in local_file_list:
    print(f'Количество слов в строке №{string_counter}: {string.count(" ") + 1}.')
    string_counter += 1

"""
Вариант подсчета через разбиение кажлой строки на список по пробелам
"""

string_counter = 1
for string in local_file_list:
    print(f'Количество слов в строке №{string_counter}: {len(string.split())}.')
    string_counter += 1
