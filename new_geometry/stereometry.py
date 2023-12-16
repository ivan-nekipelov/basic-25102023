import math

class Ball:
    def __init__(self, r):
        self.r = r

    def volume(self):
        return round((4 * math.pi * self.r**3) / 3, 5)
    
class Cube:
    def __init__(self, a):
        self.a = a

    def area(self):
        return 6*self.a**2