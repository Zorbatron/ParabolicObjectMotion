import math
from os import system, name
from tabulate import tabulate

object_ay = -9.81

roundingAmount = 2

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

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

clear()

object_vf = math.sqrt(object_vix**2 + (-object_viy)**2)

object_ty = (-object_viy)/(-9.81)
object_tx = 2 * object_ty

object_dx = object_vix * object_tx
object_dy = (object_viy * object_ty) + (0.5*object_ay*(object_ty**2)) 

data = [
    ["Vi", round(object_vix, roundingAmount), round(object_viy, roundingAmount)],
    ["Vf", round(object_vix, roundingAmount), round(-object_viy, roundingAmount)],
    ["a", "0", round(object_ay, roundingAmount)],
    ["d", round(object_dx, roundingAmount), round(object_dy, roundingAmount)],
    ["t", round(object_tx, roundingAmount), round(object_ty, roundingAmount)]
]

print(tabulate(data, headers=["Variable", "x", "y"]))
print("Object's angle was:", round(object_thetaRadians*180/math.pi, 2))