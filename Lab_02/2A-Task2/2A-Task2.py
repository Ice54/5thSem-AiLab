import math
from basic import *


class s_calc(basic_calc):
    def __init__(self, a, b):
        basic_calc.__init__(self, a, b)

    def power(self):
        return self.a ** self.b

    def log(self):
        return math.log10(self.a)

    def exp(self):
        return math.exp(self.a)

    def ln(self):
        return math.log(self.a)

    def factorial(self):
        return math.factorial(self.a)

