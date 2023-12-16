import math

class Ball:
    def __init__(self, r):
        self.r = r

    def volume(self):
        return round((4 * math.pi * self.r**3) / 3, 5)