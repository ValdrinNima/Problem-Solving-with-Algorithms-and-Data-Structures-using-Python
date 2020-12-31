"""
In many ways it would be better if all fractions were maintained in lowest terms right from the start. 
Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately. 
Notice that this means the __add__ function no longer needs to reduce. Make the necessary modifications.
"""


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        # Solution
        gcd = self.gcd(top, bottom)
        self.num = top//gcd
        self.den = bottom//gcd

    def gcd(self, m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + \
            self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum


x = Fraction(1, 2)
y = Fraction(2, 3)
z = Fraction(12, 36)

print(z.show())
print(x+y)
print(x == y)
