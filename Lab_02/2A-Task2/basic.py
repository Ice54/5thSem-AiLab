class basic_calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.a == 0:
            return 0
        elif self.b == 0:
            return 0
        else:
            return self.a / self.b

