number = int(input('Введите целое положительное число: '))
check_number = 0
max_number = 0
i = 10
check = True

while check:
    if number % i == number:
        check = False
    check_number = (number % i) // int(i / 10)
    i *= 10
    if check_number > max_number:
        max_number = check_number
print(max_number)
