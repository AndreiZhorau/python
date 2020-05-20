def my_func(x, y):
    """Function accepts positive int 'x' and negative int 'y'. Function returns 'x ** y'

    :param x: positive integer
    :param y: negative integer
    :return: x ^ y

    """
    if isinstance(x, int) and isinstance(y, int) and x >= 0 and y < 0:
        answer = 1
        for i in range(0, abs(y)):
            answer /= x
    else:
        answer = None
        print('Программа принимает только действительное положительное число "x" и целое отрицательное число "y".')
    return answer


x = int(input('x: '))
y = int(input('y: '))
print(x ** y)
print(my_func(x, y))
