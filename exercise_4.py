class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} начал движение.')

    def stop(self):
        print(f'Автомобиль {self.name} остановилася.')

    def turn(self, direction):
        self.direction = direction
        print(f'Автомобиль {self.name} повернул {self.direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет {self.speed}км/ч.')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет {self.speed}км/ч.')
        if self.speed > 60:
            print(f'Превышение!\nСнизьте скорость до 60км/ч. ')


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет {self.speed}км/ч.')
        if self.speed > 40:
            print(f'Превышение!\nСнизьте скорость до 40км/ч. ')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True


vw = Car(60, 'green', 'Golf')
police_car = PoliceCar(100, 'black', 'Ford')

vw.go()
vw.stop()
vw.turn('налево')
vw.show_speed()

print(vw.color, vw.name)

print(police_car.is_police)

police_car.show_speed()
