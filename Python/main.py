from tabulate import tabulate
import functions

def main():
    #Get option from the user
    match input("Enter 1 for Viy and Vix and 2 for Vi and Θ.\n"):
        case "1":
            functions.vixviy()
        case "2":
            functions.vitheta()

if __name__ == "__main__":
    main()