import math


class basic_calc:
    def __init__ (self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        if self.a == 0:
            return 0
        elif self.b == 0:
            return 0
        else:
            return self.a/self.b

class s_calc(basic_calc):
    def __init__(self,a,b):
        basic_calc.__init__(self,a,b)

    def power(self):
        return self.a**self.b

    def log(self):
        return math.log10(self.a)

    def exp(self):
        return math.exp(self.a)

    def ln(self):
        return math.log(self.a)

    def factorial(self):
        return math.factorial(self.a)

a = input("Enter first number: ")
b = input("Enter second number: ")

x = s_calc(int(a),int(b))
print("Sum =" + str(x.sum()))
print("Sub =" + str(x.sub()))
print("Multiply ="+str(x.mul()))
print("Division ="+str(x.div()))
print("Power ="+str(x.power()))
print("Log ="+str(x.log()))
print("Factorial ="+str(x.factorial()))
print("Exponential ="+str(x.exp()))
print("Natural Log ="+str(x.ln()))

