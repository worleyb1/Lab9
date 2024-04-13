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
                print("Your password has been encoded and stored!")
            else:
                print("Please enter an 8-digit password!")

        elif choice == 2:
            encoded_password = encode(password)
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")

        elif choice == 3:
            break

        else:
            print("Please enter another option!")
            continue










if __name__ == "__main__":
    main()