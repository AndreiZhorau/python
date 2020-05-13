a = int(input('Введите результат первого дня в км: '))
b = int(input('Введите целевой результат в км: '))
day_count = 1

while a < b:
    a *= 1.1
    day_count += 1
else:
    print(day_count)
