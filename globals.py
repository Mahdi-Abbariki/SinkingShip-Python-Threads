import random


def initialize(): 
    global mainShip 
    global shipThread 
    
    global boatThreads
    boatThreads = list()

    global personsThreads
    personsThreads = list()

def decomposition(i,minInt=10,max=60):
        while i > 0:
            n = random.randrange(minInt,min(max,i)) if i>=minInt else i
            yield n
            i -= n