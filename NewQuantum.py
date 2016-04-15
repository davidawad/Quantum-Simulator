import cmath

#Phase 1: Single Qubit OPerations, to be generalized to multiQubit models later

phase1 = '''
def Trivial(Qublock):
    return Qublock

def SingleHadamard(Qublock):
    return [[1/(2**0.5)*(Qublock[0][0]+Qublock[0][1]), 1/(2**(0.5))*(Qublock[0][0]- Qublock[0][1])]]


class Gate:
    def __init__(self,operator, args,name): #can be set later
        self.operator = operator
        self.args = args
        self.name = name
        self.out = []
    def fire(self):
        #We need that pass by reference! begin by emptying
        while len(self.out) > 0:
            self.out.pop(0)

        computation = self.operator(self.args)
        i = 0
        while i < len(computation):
            self.out.append(computation[i])
            i+=1

        #Now the array isn't destroyed so Reference continues!
        
        self.out = self.operator(self.args) #a tuple of vals from another point
        

class QuantumCircuit:
    #layers are tuples of gates
    #layers can be of course manipulated later
    #Now the question is the SuperPosition
    def __init__(self,layers): 
        self.layers = layers

    def evaluate(self):
        for layers in self.layers:
            for gates in layers:
                gates.fire()
        
        

    



#A simple Initialization Protocol:
#StartLayer = [Gate(Trivial,[[0,1]],"start")]
#SecondLayer = [Gate(SingleHadamard, StartLayer[0].out, "hadamard")]

#Circuit = QuantumCircuit((StartLayer, SecondLayer))

#Circuit.evaluate()

#print Circuit.layers[1][0].out

'''

#Phase 2: MultiQubit Model, in this case it is necessary to maintain a global state of superpositions:


def Trivial(Qublock):
    return Qublock

def SingleHadamard(Qublock):
    return [[1/(2**0.5)*(Qublock[0][0]+Qublock[0][1]), 1/(2**(0.5))*(Qublock[0][0]- Qublock[0][1])]]


class Gate:
    def __init__(self,operator, args,name): #can be set later
        self.operator = operator
        self.args = args
        self.name = name
        self.out = []
    def fire(self):
        #We need that pass by reference! begin by emptying
        while len(self.out) > 0:
            self.out.pop(0)

        computation = self.operator(self.args)
        i = 0
        while i < len(computation):
            self.out.append(computation[i])
            i+=1

        #Now the array isn't destroyed so Reference continues!
        
        self.out = self.operator(self.args) #a tuple of vals from another point
        

class QuantumCircuit:
    #layers are tuples of gates
    #layers can be of course manipulated later
    #Now the question is the SuperPosition
    def __init__(self,layers): 
        self.layers = layers

    def evaluate(self):
        for layers in self.layers:
            for gates in layers:
                gates.fire()



