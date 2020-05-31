from time import sleep


class TrafficLight:
    __color = ''
    cycles = 0

    def running(self, max_cycles=3):
        """
        :param max_cycles:  Number of cycles. 3 by default
        """

        while self.cycles < max_cycles:
            self.color = 'red'
            print(self.color)
            sleep(7)
            self.color = 'yellow'
            print(self.color)
            sleep(2)
            self.color = 'green'
            print(self.color)
            sleep(7)
            self.color = 'yellow'
            print(self.color)
            sleep(2)
            self.cycles += 1
        else:
            print(f'Светофор закончил работу после выполнения {self.cycles} циклов.')


tr_1 = TrafficLight()

tr_1.running(5)
