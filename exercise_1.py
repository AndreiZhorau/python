def divide(a, b):
    try:
        answer = a / b
    except ZeroDivisionError:
        answer = None
        print('Error. Division by zero.')
    return answer


print(divide(int(input('a: ')), int(input('b: '))))
