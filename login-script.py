

secret_pin = 1515
user_input = int(input("enter pin: "))
attempts = 0
pin = False

while attempts < 2:
    if user_input != secret_pin and attempts < 2:
        attempts += 1
        user_input = int(input("Wrong pin, enter pin again: "))
        if user_input == secret_pin:
            print("congrats. pin is correct")
            break
    elif user_input == secret_pin:
        print("congrats. pin is correct")
        break
else:
    print("Sorry. You have made multiple wrong attempts" + "\nPlease try again in 30mins")

