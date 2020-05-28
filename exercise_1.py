try:
    with open((input('Введите имя нового текстового файла (расширение добавляется автоматически): ') + '.txt'),
              'x', encoding='utf-8') as user_file:
        while True:
            user_input = input('Введите текст новой строки (для выхода оставьте строку пустой): ')
            if user_input == '':
                print('Конец выполнения программы.')
                break
            user_file.write(user_input + '\n')
except FileExistsError:
    print('Файл с таким именем уже существует.')
