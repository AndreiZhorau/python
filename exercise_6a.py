from sys import argv
from itertools import count

name, start_number = argv
start_number = int(start_number)

for el in count(start_number):
    if el > start_number + 10:
        break
    else:
        print(el)
