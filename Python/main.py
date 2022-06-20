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
    
    objectData = functions.InitialCalc(objectDataPreCalc)
    functions.InitialPlot(objectData)

if __name__ == "__main__":
    main()