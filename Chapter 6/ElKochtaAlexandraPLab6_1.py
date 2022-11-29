# Alexandra El Kochta
# Professor: Shah, Madhvi
# 

import re


def main():
    original_string = input("Enter a string to convert it to hackerspeak! ")
    print(hacker_speak(original_string))


    credit_card_number = input("Enter your credit card number: ")
    while (len(credit_card_number) < 14) or (len(credit_card_number) > 16):
        print("That is not a valid length for a credit card number. Please try again.")
        credit_card_number = input("Please enter a valid number: ")
    while True:
        try:
            credit_card_number = int(credit_card_number)
        except ValueError:
            print("That is not a valid credit card number (contains non-numeric data).")
            credit_card_number = input(("Please enter a valid number: "))
        else:
            print(card_hide(credit_card_number))
            break


def hacker_speak(original):
    new_string = original.replace("A", "4")
    new_string = new_string.replace("a", "4")
    new_string = new_string.replace("E", "3")
    new_string = new_string.replace("e", "3")
    new_string = new_string.replace("I", "1")
    new_string = new_string.replace("i", "1")
    new_string = new_string.replace("O", "0")
    new_string = new_string.replace("o", "0")
    new_string = new_string.replace("S", "5")
    new_string = new_string.replace("s", "5")

    return(new_string)


def card_hide(cc_number):
    cc_number = str(cc_number)
    pattern = '.'
    replacement = '*'
    if len(cc_number) == 15:
        count = 11
    elif len(cc_number) == 16:
        count = 12
    else:
        count = 10
    hidden = re.sub(pattern, replacement, cc_number, count)
    return(hidden)

if __name__ == "__main__":
    main()