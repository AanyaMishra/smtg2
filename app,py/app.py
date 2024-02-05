def ask_to_be_valentine():
    response = input("Will you be my Valentine? (yes/no): ").lower()

    if response == "yes":
        print("Yay! 🎉 Happy Valentine's Day!")
    elif response == "no":
        print("Oh, that's okay. Maybe next time. 😔")
        ask_again()
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")
        ask_to_be_valentine()

def ask_again():
    response = input("Would you like to reconsider? (yes/no): ").lower()

    if response == "yes":
        ask_to_be_valentine()
    elif response == "no":
        print("Alright, maybe another time. 😊")
    else:
        print("Invalid response. Please enter 'yes' or 'no.'")

# Run the program
ask_to_be_valentine()