def encode(string_input):
    output = 0
    j=1
    for i in string_input:
        a = (int(i) + 3) % 10
        output += (a * pow(10, len(string_input)-j))
        j+=1
    return str(output)

def decode(string_input):
    output = 0
    pwr = pow(10, len(string_input))
    for i in string_input:
        a = (int(i) - 3) % 10
        output += (a * pwr)
        pwr /= 10
    return str(output)


if __name__ == '__main__':
    encoded_password = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit")


        option = int(input("\n\nPlease enter an option: "))

        if option == 1:
            password = str(input("Please enter your password to encode: "))
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")

        elif option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decoder(encoded_password)}.\n")

        elif option == 3:
            break


