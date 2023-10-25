def main():
    pick = None
    stored_password = ''

    while pick != '3':
        print("Menu", "-------------", "1. Encode", "2. Decode", "3. Quit", "", sep="\n")
        pick = input("Please enter an option: ")

        if (pick == "1"):
            stored_password = input("Please enter your password to encode: ")
            stored_password = encode(stored_password)
            print("Your password has been encoded and stored!")
        elif (pick == "2"):
            pass #TODO implement decoder function

def encode(password):
    """Encodes the password
    
    Arguments: password (string, the password to encode)
    Returns: string"""
    encoded_password = []

    for char in password:
        encoded_password.append(str(int(char)+3))

    return encoded_password
        
if (__name__ == "__main__"):
    main()