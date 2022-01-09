##############################################
#   Written By : Mahdi Abbariki
#
#
#   if you want to see result in file for better scrolling, use this commnad
#   python3 main.py > result
#   wait for it to finish, it takes about 1 min (because of time sleep in boat class)
#   run it in console for colorings ;)
##############################################

# packages
import random
from colorama import Fore
# local files
import globals
from Classes import *


# Main thread is for Managing other threads
# Ship, Boats and Persons have their own threads
if __name__ == "__main__":

    Ship.alert()

    globals.initialize()

    globals.mainShip = Ship()
    boats = list()
    persons = list()

    # we should have enough Boats to add jackets to rescue 200-60 (140) person
    # we divide 140 into random parts (min jackets is 10 and max is 60 for each boat)
    boatsCapacities = list(globals.decomposition(
        globals.mainShip.numberOfPassengers - globals.mainShip.numberOfJackets))
    for capacity in boatsCapacities:
        boats.append(Boat(capacity))

    # init Threads
    globals.mainShip.initThread()

    # init boats with time.sleep() 
    # so boats will come between sinking the main ship 
    # and with delays between each arrival (min : 2s, max : 5s)
    sumOfSleepTime = 1
    sumList = list()
    for index, boat in enumerate(boats):
        n = random.randrange(2, 5)
        sumOfSleepTime += n
        sumList.append(sumOfSleepTime)

        boat.numberOfBoat = index+1
        boat.sumOfSleep = sumOfSleepTime
        
        boat.initThread()

    print("each Rescue Boat will come in (seconds) :")
    print(sumList)

    for index in range(constant.inShipPersonsCount):
        person = Person(index+1)
        persons.append(person)
        person.initThread()

    # Joining all Threads that has been created
    for thread in globals.personsThreads:
        thread.join()

    for thread in globals.boatThreads:
        thread.join()

    globals.shipThread.join()
