class Road:

    def __init__(self, length=1, width=1):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        mass = self._length * self._width * 125
        # 125 - масса одного кв.м асфальтового покрытия, кг
        return mass


my_road = Road(2, 2)

print(my_road.asphalt_mass())
