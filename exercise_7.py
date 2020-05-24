factorial_calc = 1


def fact(n):
    for i in range(1, n + 1):
        yield i * factorial_calc


for el in fact(5):
    print(el)
    factorial_calc = el
