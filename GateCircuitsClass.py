class LogicGate:

    def __init__(self,n):
        self.label=n
        self.output=None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output=self.performGateLogic()
        return self.output
    #at this point, we'll not implement performGateLogic function, because we don't know how each gate will perform its
    #own logic operation. Those details will be included by each individual gate that is added to the hierarchy.

class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA=None
        self.pinB=None

    def getpinA(self):
        if self.pinA==None:
            return int(input("Enter pinA input for gate"+self.getLabel()+"------>"))
        else:
            return self.pinA.getFrom().getOutput()

    def getpinB(self):
        if self.pinB==None:
            return int(input("Enter pinB input for gate" + self.getLabel() + "------>"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA==None:
            self.pinA=source
        elif self.pinB==None:
            self.pinB=source
        else:
            print("Cannot connect: NO EMPTY PINS on this gate.")

class AndGate(BinaryGate)
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a=self.getpinA()
        b=self.getpinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate)
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a=self.getpinA()
        b=self.getpinB()
        if a==1 or b==1:
            return 1
        else:
            return 0


class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin=None

    def getpin(self):
        if self.pin==None
            return int(input("Enter pin input for gate" + self.getLabel() + "------>"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin==None:
            self.pin=source
        else:
            print("Cannot connect: NO EMPTY PINS on this gate")

class NotGate(UnaryGate)
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a=self.getpin()
        if a==1:
            return 0
        elif a==0:
            return 1

class Connector
    def __init__(self,fgate,tgate):
        self.fromgate=fgate
        self.togate=tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate





