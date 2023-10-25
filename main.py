def main():
    pick = None

    while pick != '3':
        print("Menu", "-------------", "1. Encode", "2. Decode", "3. Quit", sep="\n")
        pick = input("Please enter an option: ")

        if (pick == "1"):
            pass #TODO implement encoder function
        elif (pick == "2"):
            pass #TODO implement decoder function

if (__name__ == "__main__"):
    main()