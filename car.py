import random


class Car:
    def __init__(self, acceleration, color, mark, track, symbol):
        self.acceleration = acceleration
        self.color = color
        self.mark = mark
        self.track = track
        self.symbol = symbol


car_1 = Car(random.randrange(1, 4), "black", "Ford", 1, "X")
car_2 = Car(random.randrange(1, 4), "white", "Mazda", 2, "O")