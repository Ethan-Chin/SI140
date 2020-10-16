# This part of code is to confirm the results of Exercises 39 in BH

# Running Environment: Python 3.7.6
# Running Command: 'python Prob39.py'

import random


def randomChooseWithP(p:float):
# Set the probability that Monty opens door2
    choose = random.random()

    if choose <= p:
        return 1

    return 2

class GameDoors:
# This class represents the doors in the game

    def __init__(self):

        self.doors = [False]*3
        # Using a list to represent doors, False means it is a goat door; True means it is a car door

        self.carLocated = random.randint(0, 2)
        self.doors[self.carLocated] = True
        # Randomly choose a door to be the car door

    def car(self):
        return self.carLocated
        # Return where is the car door

    def show(self, which):
        return self.doors[which]
        # Tell whether you chose the car door and win the game

class Me:
# This class represents the game player

    def __init__(self):
        pass
    
    

class Monty:
# This class represents Monty


    def __init__(self, me:Me, gamedoors:GameDoors, p:float):
        self.gamedoors = gamedoors
        self.me = me

        self.p = p
        # p is the probability that Monty opens door2

        self.carLocated = gamedoors.car()
    
    def montyChoose(self):
       
        if self.carLocated == 0:
            return randomChooseWithP(self.p)
        elif self.carLocated == 1:
            return 2
        else:
            return 1 
        # Monty choose opens a door that is neither a car door nor the player chosen door with the probability in choosing door 2
        
        
def oneceGame(mode:int, p:float):
# This is one game

    gamedoors = GameDoors()
    me = Me()
    monty = Monty(me, gamedoors, p)
    # Initialize the three parts of a game: GameDoors, a player and a Monty

    meChoose = 0
    # First monty let the player to choose door 0

    montyChoose = monty.montyChoose()
    # Then Monty opens a door

    meChoose = [1, 2]
    meChoose.remove(montyChoose)
    # the player switch the door

    if (mode == 1 and montyChoose == 2) or (mode == 2 and montyChoose == 1):
        return 'Again!'
    # If Monty didn't choose the required door in given mode, then do it again


    # mode 0 means the player always switch unconditionally (question(a)), mode 1 means given that Monty opens door 2 (quastion (b)), mode 2 means given that Monty opens door 3 (quastion (c))
    

    return gamedoors.show(meChoose[0])
    # Judge whether the player wins


def Game(mode:int, times:int, p:float):
# Set specific mode and p, then play the game repeatedly in "times". Finally we get the frequency that the player wins. When "times" is large enough, the frequency can show the probability, then return it

    win = 0
    i = 0
    while i< times:
        game = oneceGame(mode, p)

        if game == 'Again!':
            continue

        if game:
            win += 1
        i += 1
    # Count the win times
    print('After %d times playing, the frequency of wins is %.4f' % (times, win/times))
    return win/times



#--------------------------------------------------Test Case--------------------------------------------------#



SampleError = 0.02
# Set the samplingError to be 0.02 or other value
p = float(input("Please enter the p you want to check (float, >= 0.5): "))
# Set p


# Question(a)
try:
    assert(abs(Game(0, 10000, p) - 2/3) <= SampleError)
    print("The test with p = %.4f and unconditionally, Switch: CHECKED!" % (p))
except:
    print("The test with p = %.4f and unconditionally, Switch: FAILED!" % (p))

# Question(b)
try:
    assert(abs(Game(1, 10000, p) - 1/(p+1)) <= SampleError)
    print("The test with p = %.4f and given Monty opens door 2, Switch: CHECKED!" % (p))
except:
    print("The test with p = %.4f and given Monty opens door 2, Switch: FAILED!" % (p))

# Question(c)
try:
    assert(abs(Game(2, 10000, p) - 1/(2-p)) <= SampleError)
    print("The test with p = %.4f and given Monty opens door 3, Switch: CHECKED!" % (p))
except:
    print("The test with p = %.4f and given Monty opens door 3, Switch: FAILED!" % (p))
