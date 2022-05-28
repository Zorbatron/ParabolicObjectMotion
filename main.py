import math
from operator import index
import os
import sys
from tabulate import tabulate

CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 

def delete_last_lines(n): 
    for _ in range(n): 
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE) 

object_ay = -9.81
roundingAmount = 2

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

clear()

print("Enter 1 for Viy and Vix and 2 for Vi and Θ.")

match int(input()):
    case 1:
        clear()
        print("Input object's initial horizontal velocity.")
        object_vix = float(input())
        clear()

        print("Input object's initial vertical velocity.")
        object_viy = float(input())
        clear()

        object_vi = math.sqrt( object_vix**2 + object_viy**2 )
        object_thetaRadians = math.atan(object_viy/object_vix)
    case 2:
        clear()
        print("Input object's initial velocity.")
        object_vi = float(input())
        clear()

        print("Input object's angle from the horizontal in degrees.")
        object_thetaRadians = float(input()) * math.pi/180
        clear()

        object_vix = object_vi * math.cos(object_thetaRadians)
        object_viy = object_vi * math.sin(object_thetaRadians)
    case _:
        print("Invalid selection") 
        exit()

clear()

object_vf = math.sqrt(object_vix**2 + (-object_viy)**2)

object_ty = (-object_viy)/(object_ay)
object_tx = 2 * object_ty

object_dx = object_vix * object_tx
object_dy = (object_viy * object_ty) + (0.5*object_ay*(object_ty**2)) 

data = [
    ["Vi    | m/s", round(object_vix, roundingAmount), round(object_viy, roundingAmount)],
    ["Vf    | m/s", round(object_vix, roundingAmount), "0"],
    ["a     | m/s^2", "0", round(object_ay, roundingAmount)],
    ["d     | m", round(object_dx, roundingAmount), round(object_dx, roundingAmount)],
    ["t     | sec", round(object_tx, roundingAmount), round(object_ty, roundingAmount)]
]
print(tabulate(data, headers=["Variable", "x", "y"], tablefmt="grid"))

print("\nObject's angle was:", round(object_thetaRadians*180/math.pi, roundingAmount))
print("Object's Vi:", round(object_vi, roundingAmount))

print("\nCalculate distance at a certain time? y|n")
if (input() == "n"):
    exit() 

delete_last_lines(2)
print("Enter point in time at which to measure.")
object_tEval = float(input())
print("")

object_dx = object_vix * object_tEval
object_dy = (object_viy * object_tEval) + (0.5*object_ay*(object_tEval**2)) 

data = [
    ["v     | m/s", "", ""],
    ["d     | m", round(object_dx, roundingAmount), round(object_dy, roundingAmount)],
    ["t     | sec", round(object_tEval, roundingAmount), round(object_tEval, roundingAmount)]
]
print(tabulate(data, headers=["Variable @ " + str(object_tEval) + " s", "x", "y"], tablefmt="grid"))