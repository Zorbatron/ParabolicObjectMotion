import functions

def main():
    # Clear the screen.
    functions.Clear()

    # Get option from the user.
    match input("Enter 1 for Viy and Vix and 2 for Vi and Θ: "):
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
        evalType = input("\nEnter t, dx, or dy to evaluate. Anything else to exit: ")
        functions.DeleteLastLines(1)

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
                # Get distance, calculate at that distance, and plot the data.
                evalDy = float(input("Enter Vertical Distance: "))
                evalData = functions.VerticalEvaluation(evalDy, objectData)

                # "Error codes" if the requested Dy is invalid
                match evalData:
                    case 0:
                        print("Requested vertical distance is above the objects max Dy!")
                        continue
                    case 1:
                        print("Cannot evaluate at 0m")
                        continue

                # Plot the data for PreApex
                functions.EvaluationPlot(evalData[0], functions.EvalStringMaker(evalData[0][4]))
                # Plot the data for AftApex
                functions.EvaluationPlot(evalData[1], functions.EvalStringMaker(evalData[1][4]))


            case _:
                cont = False
                functions.DeleteLastLines(1)

if __name__ == "__main__":
    main()
