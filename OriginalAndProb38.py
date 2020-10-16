# This part of code is to confirm the results of original Monty Hall problem and Exercises 38 in BH

# Running Environment: Python 3.7.6
# Running Command: 'python OriginalAndProb38.py'

import random


class GameDoors:
# This class represents the doors in the game

    def __init__(self, n:int):
        self.n = n
        # n is the number of doors

        self.doors = [False]*self.n
        # Using a list to represent doors, False means it is a goat door; True means it is a car door

        self.carLocated = random.randint(0, n - 1)
        self.doors[self.carLocated] = True
        # Randomly choose a door to be the car door

    def car(self):
        return self.carLocated
        # Return where is the car door

    def numDoors(self):
        return self.n
        # Return the number of the doors

    def show(self, which):
        return self.doors[which]
        # Tell whether you chose the car door and win the game

class Me:
# This class represents the game player

    def __init__(self):
        pass

    def choose(self, chooseRange:list):
        return random.sample(chooseRange, 1)[0]
        # The player randomly choose a door in all the doors which are choosable (That is, the doors in chooseRange)
    
    

class Monty:
# This class represents Monty


    def __init__(self, me:Me, gamedoors:GameDoors, m:int):
        self.gamedoors = gamedoors
        self.me = me
        self.n = gamedoors.numDoors()
        self.m = m
        # m is the number of doors that Monty open after the player choose one

        self.carLocated = gamedoors.car()

        self.meChooseRange = list(range(self.n))
        self.montyChooseRange = self.meChooseRange[:]
        try:
            self.montyChooseRange.remove(self.carLocated)
        except:
            pass
        # Set two door lists that could be chosen by the player or Monty. There is a rule that Monty can't choose the car door, so we remove it from montyChooseRange

    def meChoose(self):
        temp = self.me.choose(self.meChooseRange)
        try:
            self.meChooseRange.remove(temp)
        except:
            pass
        try:
            self.montyChooseRange.remove(temp)
        except:
            pass
        return temp
        # Monty tells the player to choose a door in the doors that are choosable, and update the choosable doors lists.
    
    def montyChoose(self):
        temp = random.sample(self.montyChooseRange, self.m)
        for i in temp:
            try:
                self.meChooseRange.remove(i)
            except:
                pass
        return temp
        # Monty choose m doors to open and update the choosable doors lists
        
        
def oneceGame(m:int, n:int, changable:bool):
# This is one game

    gamedoors = GameDoors(n)
    me = Me()
    monty = Monty(me, gamedoors, m)
    # Initialize the three parts of a game: GameDoors, a player and a Monty

    meChoose = monty.meChoose()
    # First monty let the player to choose one door

    monty.montyChoose()
    # Then Monty chooses m doors to open

    if changable:
        meChoose = monty.meChoose()
    # Monty asks the player whether to change the door, if change then the player choose again, if not then keep the original chosen door
    
    return gamedoors.show(meChoose)
    # Judge whether the player wins


def GamePrint(m:int, n:int, changable:bool, times:int):
#Set specific m and n, then play the game repeatedly in "times". Finally we get the frequency that the player wins. When "times" is large enough, the frequency can show the probability, then print it

    win = 0
    for i in range(times):
        if oneceGame(m, n, changable):
            win += 1
    # Count the win times

    if changable:
        print("With m = %d and n = %d. After %d games and always switch, you won %d times and the frequency of win is %.4f" % (m, n, times, win, win/times))
    
    else:
        print("With m = %d and n = %d. After %d games and always not switch, you won %d times and the frequency of win is %.4f" % (m, n, times, win, win/times))


def Game(m:int, n:int, changable:bool, times:int):
#Set specific m and n, then play the game repeatedly in "times". Finally we get the frequency that the player wins. When "times" is large enough, the frequency can show the probability, then return it

    win = 0
    for i in range(times):
        if oneceGame(m, n, changable):
            win += 1
    # Count the win times

    return win/times



#--------------------------------------------------Test Case--------------------------------------------------#


GamePrint(1, 3, True, 10000)
GamePrint(1, 3, False, 10000)
# Confirm the result in original Monty Hall problem that m = 1, n = 3


GamePrint(3, 7, True, 10000)
GamePrint(3, 7, False, 10000)
# Confirm the result in Prob.38(a) in BH where m = 3, n = 7

print('Now lets check Prob.38(b) in BH')


############################Confirm the result in Prob.38(b) in BH##############################
                                                                                               #
                                                                                               #
# Where m ranges from 1 to n-1;n can be any number over 3, here we set n ranges from 3 to maxN.#
SampleError = 0.02                                                                             #
# Set the samplingError to be 0.02 or other value                                              #
maxN = int(input("Please enter the max n you want to check: "))                                #
for n in range(3, maxN+1):                                                                     #
    for m in range(1, n-1):                                                                    #
        try:                                                                                   #
            assert(abs(Game(m, n, False, 10000) - 1/n) <= SampleError)                         #
            print("The test with m = %d, n = %d, No Switch: CHECKED!" % (m, n))                #
        except:                                                                                #
            print("The test with m = %d, n = %d, No Switch: FAILED!" % (m, n))                 #
        try:                                                                                   #
            assert(abs(Game(m, n, True, 10000) - (1/n)*((n-1)/(n-m-1))) <= SampleError)        #
            print("The test with m = %d, n = %d, Do Switch: CHECKED!" % (m, n))                #
        except:                                                                                #
            print("The test with m = %d, n = %d, Do Switch: FAILED!" % (m, n))                 #
################################################################################################
