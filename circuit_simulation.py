# Brian P. Steffes
# Problem Solving w/ Algorithms and Data Structures
# July 24, 2016


class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        # function perform_gate_logic() to be implemented in subclasses.
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        # Child Constructors follow initialization of Parent Constructors.
        self.pinA = None
        self.pinB = None

    def get_pinA(self):
        return int(raw_input("Enter Pin A input for gate {0} --> ".format(self.get_label())))

    def get_pinB(self):
        return int(raw_input("Enter Pin B input for gate {0} --> ".format(self.get_label())))


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        if a == 0 and b == 0:
            return 0
        else:
            return 1


class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def get_pin(self):
        return int(raw_input("Enter Pin input for gate {0} --> ".format(self.get_label())))

class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def perform_gate_logic(self):
        return self.get_pin()



class Connector:

    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate
        





