def search_number(user_string):
    """
    Принимает строку, возвращает int(числовые символы в строке).
    """

    number = ''
    for character in user_string:
        if character.isdigit():
            number += character
    try:
        number = int(number)
    except ValueError:
        number = 0
    return number


subjects_dict = {}

with open('text_6.txt', 'r', encoding='utf-8') as subjects:
    for line in subjects:
        subject, lecture_hours, practice_hours, laboratory_hours = line.split()
        subjects_dict[subject] = search_number(lecture_hours) + search_number(practice_hours) + search_number(
            laboratory_hours)

print(subjects_dict)
