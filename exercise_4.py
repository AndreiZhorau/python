from googletrans import Translator

translator = Translator()

with open('text_4.txt', 'r', encoding='utf-8') as local_file_en, open('text_4_ru.txt', 'w+',
                                                                      encoding='utf-8') as local_file_ru:
    for line in local_file_en:
        eng_number = line.split()[0]
        ru_number = translator.translate(eng_number, src='en', dest='ru').text
        local_file_ru.write(f'{line.replace(eng_number, ru_number)}')

    local_file_en.seek(0)
    local_file_ru.seek(0)
    print(f'Исходный файл:\n{local_file_en.read()}\nНовый файл:\n{local_file_ru.read()}')
