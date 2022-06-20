# The objectData list ALWAYS goes: 
# objectVix, objectViy, objectVi, objectThetaRadians, 
# objectTx, objectTy, objectDx, ObjectDy.
objectData = []

# The evalData list ALWAYS goes: objectVx, objectVy, objectDx, objectDy.
evalData = []

from tabulate import tabulate
from os import system, name
import constants
import sys
import math

# Magic code to delete only the last n lines in the terminal.
def DeleteLastLines(n): 
    for _ in range(n): 
        sys.stdout.write(constants.CURSOR_UP_ONE) 
        sys.stdout.write(constants.ERASE_LINE) 

# Clear the screen depending on the OS
def Clear():
    _ = system('cls') if name == 'nt' else system('Clear')

# Getting the values depending on the horizontal and vertical components of the initial velocity.
def VixViy():
    Clear()
    objectVix = float(input("Input object's initial horizontal velocity.\n"))
    Clear()

    objectViy = float(input("Input object's initial vertical velocity.\n"))
    Clear()

    objectVi = math.sqrt( objectVix**2 + objectViy**2 )
    objectThetaRadians = math.atan(objectViy/objectVix)

    objectData.append(objectVix)
    objectData.append(objectViy)
    objectData.append(objectVi)
    objectData.append(objectThetaRadians)

    return objectData

# Getting the values depending on the initial velcities resultant vector and it's angle to the horizontal.
def ViTheta():
    Clear()
    objectVi = float(input("Input object's initial velocity.\n"))
    Clear()

    objectThetaRadians = float(input("Input object's angle from the horizontal in degrees.\n")) * math.pi/180
    Clear()

    objectVix = objectVi * math.cos(objectThetaRadians)
    objectViy = objectVi * math.sin(objectThetaRadians)
    
    objectData.append(objectVix)
    objectData.append(objectViy)
    objectData.append(objectVi)
    objectData.append(objectThetaRadians)

    return objectData

# The first calculation to determine distance travelled and how long it took.
def InitialCalc(objectDataPreCalc):
    objectTy = (-objectDataPreCalc[1])/(constants.objectAy)
    objectTx = objectTy * 2

    objectDx = objectDataPreCalc[0] * objectTx
    objectDy = (objectDataPreCalc[1] * objectTy) + (0.5*constants.objectAy*(objectTy**2)) 

    objectDataPreCalc.append(objectTx)
    objectDataPreCalc.append(objectTy)
    objectDataPreCalc.append(objectDx)
    objectDataPreCalc.append(objectDy)

    return objectDataPreCalc

# The function to plot the first set of data.
def InitialPlot(objectDataToPlot):
    plotData = [
    ["Vi    |   m/s", round(objectDataToPlot[0], constants.roundingAmount), round(objectDataToPlot[1], constants.roundingAmount)],
    ["Vf    |   m/s", round(objectDataToPlot[0], constants.roundingAmount), "0"],
    ["a     |   m/s^2", constants.objectAx, round(constants.objectAy, constants.roundingAmount)],
    ["d     |   m", round(objectDataToPlot[6], constants.roundingAmount), round(objectDataToPlot[7], constants.roundingAmount)],
    ["t     |   sec", round(objectDataToPlot[4], constants.roundingAmount), round(objectDataToPlot[5], constants.roundingAmount)]
    ]

    print(tabulate(plotData, headers=["Variable", "x", "y"], tablefmt="grid", disable_numparse=True))

    print("\nΘ: ", round(objectData[3]*180/math.pi, constants.roundingAmount), "\b°")
    print("Vi:", round(objectData[2], constants.roundingAmount), "m/s")

# The function to plot the evaluation data
# The evalString should look something like this: "Data @ 2.1s" or "Data @ 5.2m"
def EvaluationPlot(evalData, evalString):
    data = [
        ["v     |   m/s", round(evalData[0], constants.roundingAmount), round(evalData[1], constants.roundingAmount)],
        ["d     |   m", round(evalData[2], constants.roundingAmount), round(evalData[3], constants.roundingAmount)]
    ]
    print(tabulate(data, headers=[evalString, "x", "y"], tablefmt="grid", disable_numparse=True))

# Evaluate at a certain time.
def TimeEvaluation(evalTime, objectData):
    DeleteLastLines(1)

    evalDx = objectData[0] * evalTime
    evalDy = (objectData[1] * evalTime) + (0.5*constants.objectAy*(evalTime**2))

    evalVx = objectData[0] + (evalTime*constants.objectAx)
    evalXy = objectData[1] + (evalTime*constants.objectAy)

    evalData.append(evalVx)
    evalData.append(evalXy)
    evalData.append(evalDx)
    evalData.append(evalDy)

    return evalData

# Evaluate at a certain X distance.
def HorizontalEvaluation(evalDx, objectData):
    print("Horizontal Evaluation Selected!")

# Evaluate at a certain Y distance.
def VerticalEvaluation(evalDy, objectData):
    print("Vertical Evaluation Selected!")