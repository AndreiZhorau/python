revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))

if revenue > costs:
    print(f'Фирма работает с прибылью.\nРентабильность фирмы составила: {(revenue - costs) / costs:.2f}')
    employee = int(input('Введите численность сотрудников фирмы: '))
    print(f'Прибыль фирмы в расчете на сотрубника составила: {(revenue - costs) / employee:.2f}')
else:
    print('Фирма работает с убытками.')
