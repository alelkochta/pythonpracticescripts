# El Kochta, Alexandra
# Shah, Madhvi 
# CMSC 135 
# 10/14/22
#Definition main function
#	Prompt user for text to encode 
#	Prompt user for shift amount 
#	Pass text and shift amount to caesar_shift function and set the result to variable new_text 
#	DISPLAY new_text 
#Definition caesar_shift function with parameters string and shift 
#	INITIALIZE encoded_string as empty string 
#	CALCULATE remainder of shift divided by 26 and set to shift 
#	For each character in string 
#		IF character = “ “ THEN 
#			set encoded_character to character
#		ELSE 
#			IF character is uppercase 
#				IF character ASCII value + shift <= 90 THEN
#					set encoded_character to ASCII character of (ASCII value of character + shift) 
#				ELSE 
#					set encoded_character to (ASCII character of (ASCII value of character + shift) -26)
#			ELSE 
#				IF character ASCII value + shift <= 122 THEN 
#				    set encoded_character to ASCII character of (ASCII value of character + shift) 
#               ELSE
#					set encoded_character to (ASCII character of (ASCII value of character + shift) -26)
#		APPEND encoded_character to encoded_string 
#	RETURN encoded_string 
#CALL main function 

# Prompts user for string and shift and calls caesar_shift funtion with those as arguments
def main():
    text = input("Enter your text to endode: ")
    shift = int(input("Enter the shift amount: "))

    new_text = caesar_shift(text, shift)
    print(new_text)

# Uses parametes of the string and the shift amount to return the new string
def caesar_shift(text, key):
    key %= 26
    encoded_string = ""
    # Loops through every letter in the string
    for i in text:
        # Skips spaces
        if i == " ":
            encoded_character = i
        else:
        # if i is uppercase
           if i.isupper():
            if (ord(i) + key) <= 90:
                encoded_character = chr(ord(i) + key)
            # allows looparound
            else:
                encoded_character = chr((ord(i) + key) - 26)
        # if i is lowercase
           else:
            if (ord(i) + key) <= 122:
                encoded_character = chr(ord(i) + key)
            # allows looparound
            else:
                encoded_character = chr((ord(i) + key) - 26)
        # Concatenate (add) the new chatacter to the new string 
        encoded_string += encoded_character
    return encoded_string

# Calls the main function
main()