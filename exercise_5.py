from functools import reduce


def my_function(previous_el, el):
    return previous_el * el


new_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(my_function, new_list))

"""
Ниже проверка решения через более очевидный цикл
"""

test_calculation = 1
for i in new_list:
    test_calculation *= i

print(test_calculation)
