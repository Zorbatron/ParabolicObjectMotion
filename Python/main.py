import functions

def main():
    # Clear the screen.
    functions.Clear()

    # Get option from the user.
    match input("Enter 1 for Viy and Vix and 2 for Vi and Θ.\n"):
        case "1":
            objectDataPreCalc = functions.VixViy()

        case "2":
            objectDataPreCalc = functions.ViTheta()

        case _:
            functions.DeleteLastLines(2)
            exit()

    # Call the first calculation stage
    objectData = functions.InitialCalc(objectDataPreCalc)

    # Call the plotting function with the first calculation stage as it's input.
    functions.InitialPlot(objectData)

    # The time/distance evaluation loop.
    cont = True
    while cont:
        evalType = input("\nEnter t, dx, or dy to evaluate. Anything else to exit\n")
        functions.DeleteLastLines(2)

        match evalType:
            case "t": 
                # Get time, calculate at that time, and plot the data.
                evalTime = float(input("Enter Time: "))
                evalData = functions.TimeEvaluation(evalTime, objectData)
                functions.EvaluationPlot(evalData, functions.EvalStringMaker(evalData[4]))

            case "dx":
                # Get distance, calculate at that distance, and plot the data.
                evalDx = float(input("Enter Horizontal Distance: "))
                evalData = functions.HorizontalEvaluation(evalDx, objectData)
                functions.EvaluationPlot(evalData, functions.EvalStringMaker(evalData[4]))

            case "dy":

                # DO NOT USE. I HAVEN'T IMPLEMENTED THE VERTICAL EVALUATION FUNCTION YET!!!!!

                # Get distance, calculate at that distance, and plot the data.
                evalDy = float(input("Enter Horizontal Distance: "))
                evalData = functions.VerticalEvaluation(evalDy, objectData)
                #functions.EvaluationPlot(evalData, "Data @ " + str(evalDy) + " m")

            case _:
                cont = False
                functions.DeleteLastLines(1)

if __name__ == "__main__":
    main()