from itertools import cycle

counter = 0
for el in cycle('Hello World!'):
    if counter > 11:
        break
    else:
        print(el)
        counter += 1



