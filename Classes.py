# packages
import threading
import time
from colorama import Fore
# local files
import globals
import constant

###########################


class Ship:
    def __init__(self):
        self.numberOfJackets = constant.initialJackets
        self.numberOfPassengers = constant.inShipPersonsCount
        self.lock = threading.Semaphore(constant.initialJackets)

    def initThread(self):
        globals.shipThread = threading.Thread(
            target=Ship.thread_function, args=(self,))
        globals.shipThread.start()

    def thread_function(self):
        while(self.numberOfPassengers > 0):
            time.sleep(1)
        Ship.finish()

    def alert():
        print(Fore.RED+" =============================================")
        print(Fore.RED+" The Ship Is Sinking, Start The Rescue Process")
        print(Fore.RED+" =============================================")
        print("\n")

    def finish():
        print("\n\n")
        print(Fore.GREEN+" =============================================")
        print(Fore.GREEN+" Congratulations!!")
        print(Fore.GREEN+" All Passengers rescued successfully !!!!")
        print(Fore.GREEN+" =============================================")


###########################


class Boat:
    def __init__(self, numberOfJackets):
        self.numberOfJackets = numberOfJackets
        self.numberOfBoat = 0
        self.sumOfSleep = 0

    def addJacket(self):
        print("want to add jacket : " + str(self.numberOfJackets))

    def initThread(self):
        x = threading.Thread(target=Boat.thread_function, args=(self,))
        globals.boatThreads.append(x)
        x.start()

    def thread_function(self):
        time.sleep(self.sumOfSleep)
        globals.mainShip.numberOfJackets += self.numberOfJackets
        for i in range(self.numberOfJackets):
            globals.mainShip.lock.release()
        print(Fore.LIGHTBLUE_EX+" Boat #"+str(self.numberOfBoat)+" has Arrived contaning "+ str(self.numberOfJackets)+" Jackets")



###########################


class Person:

    def __init__(self,numberOfPerson):
        self.numberOfPerson = numberOfPerson

    def takeJacket():
        print('want to take jacket')

    def initThread(self):
        x = threading.Thread(target=Person.thread_function, args=(self,))
        globals.personsThreads.append(x)
        x.start()

    def thread_function(self):
        globals.mainShip.lock.acquire()
        globals.mainShip.numberOfJackets -= 1
        globals.mainShip.numberOfPassengers -= 1
        print(Fore.LIGHTYELLOW_EX+" Person #"+str(self.numberOfPerson)+" has been RESCUED")



