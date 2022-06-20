import functions

def main():
    #Clear the screen.
    functions.Clear()

    #Get option from the user.
    match input("Enter 1 for Viy and Vix and 2 for Vi and Θ.\n"):
        case "1":
            objectDataPreCalc = functions.VixViy()

        case "2":
            objectDataPreCalc = functions.ViTheta()

        case _:
            exit()

    #Call the first calculation stage
    objectData = functions.InitialCalc(objectDataPreCalc)

    #Call the plotting function with the first calculation stage as it's input.
    functions.InitialPlot(objectData)

    #The time/distance evaluation loop.
    cont = True
    while cont:
        evalType = input("\nEnter t, dx, or dy to evaluate. Anything else to exit\n")
        functions.DeleteLastLines(2)

        match evalType:
            case "t":
               evalTime = float(input("Enter time: "))
               evalData = functions.TimeEvaluation(evalTime, objectData)
               functions.EvaluationPlot(evalData, "Data @ " + str(evalTime) + " s")

            case "dx":
               functions.HorizontalEvaluation()

            case "dy":
               functions.VerticalEvaluation() 

            case _:
                cont = False
                functions.DeleteLastLines(1)

if __name__ == "__main__":
    main()