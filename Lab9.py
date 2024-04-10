def main():
    while True:
        print("Menu\n----------\n1. Encode\n2. Decode\n3. Quit")
        choice = input("Please enter an option: ")
        if choice == "1":
            passcode = input("Please enter your password to encode: ")
            encoded = encoder(passcode)
            print("Your password has been encoded and stored!\n")
        elif choice == "2":
            decoded = decoder(encoded)
            print("The encoded password is "+encoded+", and the original password is", decoded+".\n")
        elif choice == "3":
            return False


def encoder(password):
    encoding = []
    output = " "
    for num in password:
        encoding.append(int(num))
    for num in encoding:
        num += 3
        output += str(num)
    return output


if __name__ == "__main__":
    main()
