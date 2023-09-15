import math


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return round(self.x * other.x + self.y * other.y, 3)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def vec_input(self, number_of_vector=1):
        print('\nEntering vector №{}: '.format(number_of_vector))
        print('Enter X, Y: ')
        x, y = map(float, input().split())
        return Vector(x, y)

    def output(self):
        print('X, Y = {}, {}'.format(self.x, self.y))

    def len(self):
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 3)


def vectors_angle(vec1, vec2):
    return round(math.acos(vec1 * vec2 / (vec1.len() * vec2.len())) * 180 / math.pi, 3)



