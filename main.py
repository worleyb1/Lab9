#Lab 9

def encode(password):
    encoded_password = ""
    for char in password:
        if char.isdigit():
            encoded_digit = (int(char) + 3) % 10
            encoded_password += str(encoded_digit)
        else:
            encoded_password += char
    return encoded_password

def decode(num):

    decoded = ""

    for char in num:
        if char == "0":
            decoded += "7"
        elif char == "1":
            decoded += "8"
        elif char == "2":
            decoded += "9"
        elif char == "3":
            decoded += "0"
        elif char == "4":
            decoded += "1"
        elif char == "5":
            decoded += "2"
        elif char == "6":
            decoded += "3"
        elif char == "7":
            decoded += "4"
        elif char == "8":
            decoded += "5"
        elif char == "9":
            decoded += "6"

    return decoded

def main():
    while True:

        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        choice = int(input("Please enter an option: "))
        password = 0

        if choice == 1:
            password = input("Please enter your password to encode: ")
            if len(password) == 8:
                encoded_password = encode(password)

                print("Your password has been encoded and stored!")
                print()
            # else:
            #     print("Please enter an 8-digit password!")

        elif choice == 2:
            decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
            print()

        elif choice == 3:
            break

        else:
            print("Please enter another option!")
            continue










if __name__ == "__main__":
    main()