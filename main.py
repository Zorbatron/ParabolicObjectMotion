import math
from tabulate import tabulate

object_ay = -9.81

print("Enter 1 for Viy and Vix and 2 for Vi and Θ.")

match int(input()):
    case 1:
        print("Input object's initial horizontal velocity.")
        object_vix = float(input())

        print("Input object's initial vertical velocity.")
        object_viy = float(input())

        object_vi = math.sqrt( object_vix**2 + object_viy**2 )
        object_thetaRadians = math.atan(object_viy/object_vix)
    case 2:
        print("Input object's initial velocity.")
        object_vi = float(input())

        print("Input object's angle from the horizontal in degrees.")
        object_thetaRadians = float(input()) * math.pi/180

        object_vix = object_vi * math.cos(object_thetaRadians)
        object_viy = object_vi * math.sin(object_thetaRadians)
    case _:
        print("Invalid selection") 

object_vf = math.sqrt(object_vix**2 + (-object_viy)**2)

object_ty = (-object_viy)/(-9.81)
object_tx = 2 * object_ty

object_dx = object_vix * object_tx
object_dy = (object_viy * object_ty) + (0.5*object_ay*(object_ty**2)) 

data = [
    ["Vi", round(object_vix), round(object_viy)],
    ["Vf", round(object_vix), round(-object_viy)],
    ["a", "0", round(object_ay)],
    ["d", round(object_dx), round(object_dy)],
    ["t", round(object_tx), round(object_ty)]
]

print(tabulate(data, headers=["Variable", "x", "y"]))
print("Object's angle was:", (object_thetaRadians*180/math.pi))