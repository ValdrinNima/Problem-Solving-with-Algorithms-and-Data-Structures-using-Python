"""
Research the __repr__ method. How does it differ from __str__? When is it used? Implement __repr__.
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
        if type(top) == int and type(bottom) == int:
            gcd = self.gcd(top, bottom)
            self.num = top//gcd
            self.den = bottom//gcd
        else:
            raise Exception("numerator and denominator must be integers")

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

    # Solution
    def __repr__(self):
        return f"Fraction({self.num}, {self.den})" 

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other):
        newnum = self.num*other.den + \
            self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __radd__(self, other):
        newnum = self.num*other.den + \
            self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __iadd__(self, other):
        newnum = self.num*other.den + \
            self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __sub__(self, other):
        newnum = self.num*other.den - self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)

    def __gt__(self, other):
        if (self.num * 1/self.den) > (other.num * 1/other.den):
            return True
        else:
            return False

    def __ge__(self, other):
        if (self.num * 1/self.den) >= (other.num * 1/other.den):
            return True
        else:
            return False

    def __lt__(self, other):
        if (self.num * 1/self.den) < (other.num * 1/other.den):
            return True
        else:
            return False

    def __le__(self, other):
        if (self.num * 1/self.den) <= (other.num * 1/other.den):
            return True
        else:
            return False

    def __ne__(self, other):
        if (self.num * 1/self.den) != (other.num * 1/other.den):
            return True
        else:
            return False

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum


x = Fraction(1, 2)
y = Fraction(2, 3)
z = Fraction(12, 36)

x += y
print(repr(x))

# print(x * y)
# print(x - y)
# print(x+y)
# print(x == y)
