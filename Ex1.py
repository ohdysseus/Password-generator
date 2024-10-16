import random

def random_char():
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/?!_-=@$#%&"
    return random.choice(char)

def generate_password():
    strength = int(input("Please enter desired amount of characters for your random password: "))

    if strength <= 0:
        print("Please enter a positive number.")
        return

    pw = "".join(random_char() for i in range(strength))
    print("Secret random password:\n" + pw)

generate_password()




