from os import *
import os

# import only system from os 
from os import system, name 
from time import sleep
# import sleep to show output for some time period 


# define our clear function 
def clear(): 
    os.system('cls' if os.name == 'nt' else 'clear')

plate = [["T", "C", "F", "D", "R", "F", "C", "T"],
         ["P", "P", "P", "P", "P", "P", "P", "P"],
         ["#", "#", "#", "#", "#", "#", "#", "#"],
         ["#", "#", "#", "#", "#", "#", "#", "#"],
         ["#", "#", "#", "#", "#", "#", "#", "#"],
         ["#", "#", "#", "#", "#", "#", "#", "#"],
         ["p", "p", "p", "p", "p", "p", "p", "p"],
         ["t", "c", "f", "d", "r", "f", "c", "t"]]
def platePrint(plate):
    for i in range(8):
        print("|", 8 - i, "||", end=" ")
        for v in range(8):
            print(plate[i][v], end=" | ")
        print("")
        if not i == 7:
            print("--------------------------------------")
    print("--------------------------------------")
    print("| 0 || a | b | c | d | e | f | g | h |")
platePrint(plate)
sleep(2)

