
stored_pass = ""

def decode():
    orig_input = ""
    for char in stored_pass:
        char = int(char)
        char -= 3
        char = str(char)
        orig_input += char
    print(f'The encoded password is {stored_pass}, and the original password is {orig_input}.')


decode()



