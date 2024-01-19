import random

def generate_password(password_length, combined):
    password = ""
    for i in range(password_length):
        char = random.choice(combined)
        password += char
    return password

if __name__ == "__main__":
    cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_lett = 'abcdefghijklmnopqrstuvwxyz'
    special_char = '!@#$%^&*()-_.'
    numbers = "0123456789"
    combined = cap_letters+small_lett+special_char+numbers
    length = int(input("Enter the desired length of password : "))
    print(generate_password(length, combined))

