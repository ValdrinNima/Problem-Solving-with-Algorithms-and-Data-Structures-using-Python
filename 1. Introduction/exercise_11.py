
"""
The most simple arithmetic circuit is known as the half-adder.
Research the simple half-adder circuit. Implement this circuit.
"""


class LogicGate:

    def __init__(self, n):
        self.name = n
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")



class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

# Solution NAND Gate


class NandGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 0
        else:
            return 1


class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


# Solution NOR Gate
class NorGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 1
        else:
            return 0

# Solution XOR Gate


class XorGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if (a == 0 and b == 1) or (b == 0 and a == 1):
            return 1
        else:
            return 0


class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

# Solution Half Adder
class HalfAdder(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)
        self.sum = None
        self.carry = None

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a == 0 and b == 1) or (b == 0 and a == 1):
            self.carry = 0
            self.sum = 1
        elif a == 1 and b == 1:
            self.carry = 1
            self.sum = 0
        else:
            self.carry = 0
            self.sum = 0
        
        return (self.sum, self.carry)

class FullAdder(BinaryGate):

    def __init__(self):
        BinaryGate.__init__(self, n)



class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def main():
    # g1 = AndGate("G1")
    # g2 = AndGate("G2")
    # g3 = OrGate("G3")
    # g4 = NotGate("G4")
    # g5 = NandGate("G5")
    # g6 = XorGate("G6")
    # g7 = NorGate("G7")
    # c1 = Connector(g1, g3)
    # c2 = Connector(g2, g3)
    # c3 = Connector(g3, g4)
    halfAdder = HalfAdder("test")

    print("hello worl")

    print(halfAdder.getOutput())


main()
