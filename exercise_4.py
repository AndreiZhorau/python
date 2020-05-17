user_string = input('Введите строку из нескольких слов разделенную пробелами: ')

user_list = user_string.split()

for i in range(0, len(user_list)):
    print(f'{i + 1}. {user_list[i][0:10]}')

print(user_list)
