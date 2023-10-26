
def main():
    pick = None
    stored_password = ''
    orig_input = ''
    while pick != '3':
        print("Menu", "-------------", "1. Encode", "2. Decode", "3. Quit", "", sep="\n")
        pick = input("Please enter an option: ")

        if (pick == "1"):
            stored_password = input("Please enter your password to encode: ")
            stored_password = encode(stored_password)
            print("Your password has been encoded and stored!")
        elif (pick == "2"):
            for char in stored_password:
                char = int(char)
                char -= 3
                char = str(char)
                orig_input += char
            print(f'The encoded password is {stored_password}, and the original password is {orig_input}.')

def encode(password):
    """Encodes the password
    
    Arguments: password (string, the password to encode)
    Returns: string"""
    encoded_password = []

    for char in password:
        encoded_password.append(str(int(char)+3))

    return ''.join(encoded_password)
        
if (__name__ == "__main__"):
    main()

