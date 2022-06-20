import math
from os import system, name
import sys
from tabulate import tabulate

CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 

def delete_last_lines(n): 
    for _ in range(n): 
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE) 

def clear():
    _ = system('cls') if name == 'nt' else system('clear')
    
object_ay = -9.81
object_ax = 0.0

roundingAmount = 2

clear()

match input("Enter 1 for Viy and Vix and 2 for Vi and Θ.\n"):
    case "1":
        clear()
        object_vix = float(input("Input object's initial horizontal velocity.\n"))
        clear()

        object_viy = float(input("Input object's initial vertical velocity.\n"))
        clear()

        object_vi = math.sqrt( object_vix**2 + object_viy**2 )
        object_thetaRadians = math.atan(object_viy/object_vix)
    case "2":
        clear()
        object_vi = float(input("Input object's initial velocity.\n"))
        clear()

        object_thetaRadians = float(input("Input object's angle from the horizontal in degrees.\n")) * math.pi/180
        clear()

        object_vix = object_vi * math.cos(object_thetaRadians)
        object_viy = object_vi * math.sin(object_thetaRadians)
    case _:
        print("Invalid selection.") 
        exit()

clear()

object_vf = math.sqrt(object_vix**2 + (-object_viy)**2)

object_ty = (-object_viy)/(object_ay)
object_tx = 2 * object_ty

object_dx = object_vix * object_tx
object_dy = (object_viy * object_ty) + (0.5*object_ay*(object_ty**2)) 

data = [
    ["Vi    |   m/s", round(object_vix, roundingAmount), round(object_viy, roundingAmount)],
    ["Vf    |   m/s", round(object_vix, roundingAmount), "0"],
    ["a     |   m/s^2", "0", round(object_ay, roundingAmount)],
    ["d     |   m", round(object_dx, roundingAmount), round(object_dy, roundingAmount)],
    ["t     |   sec", round(object_tx, roundingAmount), round(object_ty, roundingAmount)]
]
print(tabulate(data, headers=["Variable", "x", "y"], tablefmt="grid", disable_numparse=True))

print("\nΘ: ", round(object_thetaRadians*180/math.pi, roundingAmount), "\b°")
print("Vi:", round(object_vi, roundingAmount), "m/s")

cont = True
while cont:
    evalType = input("\nEnter t, dx, or dy to evaluate. Anything else to exit\n")
    delete_last_lines(2)

    if evalType == "t":
        object_tEval = float(input("Enter time: "))
        delete_last_lines(1)

        object_dx = object_vix * object_tEval
        object_dy = (object_viy * object_tEval) + (0.5*object_ay*(object_tEval**2)) 

        object_vx = object_vix + (object_tEval*object_ax)
        object_vy = object_viy + (object_tEval*object_ay)

        data = [
            ["v     |   m/s", round(object_vx, roundingAmount), round(object_vy, roundingAmount)],
            ["d     |   m", round(object_dx, roundingAmount), round(object_dy, roundingAmount)]
        ]
        print(tabulate(data, headers=["Data @ " + str(round(object_tEval, roundingAmount)) + " s", "x", "y"], tablefmt="grid", disable_numparse=True))
    elif evalType == "dx":
        object_dxEval = float(input("Enter horizontal distance: "))
        print()

        object_tEval = object_dxEval/object_vix

        object_dx = object_vix * object_tEval
        object_dy = (object_viy * object_tEval) + (0.5*object_ay*(object_tEval**2)) 

        object_vx = object_vix + (object_tEval*object_ax)
        object_vy = object_viy + (object_tEval*object_ay)

        data = [
            ["v     |   m/s", round(object_vx, roundingAmount), round(object_vy, roundingAmount)],
            ["d     |   m", round(object_dx, roundingAmount), round(object_dy, roundingAmount)]
        ]
        print(tabulate(data, headers=["Data @ " + str(round(object_tEval, roundingAmount)) + " s", "x", "y"], tablefmt="grid", disable_numparse=True))
    elif evalType == "dy":
        object_dyEval = input("Enter vertical distance: ")

        print("Just kidding, I haven't implemented this feature yet lol!")
    else:
        cont = False
        delete_last_lines(1)