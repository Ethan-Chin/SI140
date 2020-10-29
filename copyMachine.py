import random

def copyPaper(n:int):
    for m in range(int(n/2), n):
        suc = 0

        for i in range(1000):
            tray0 = tray1 = m

            for j in range(n):

                if random.randint(0, 1):
                    tray1 -= 1

                else:
                    tray0 -= 1

                if tray0 < 0 or tray1 < 0:
                    break
            
            else:
                suc += 1

        if (suc / 1000) >= 0.95:
            return m
    
n = int(input("Please enter the n: "))

print("The smallest m is: ", copyPaper(n))
    
