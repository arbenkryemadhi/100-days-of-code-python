import os
from os import sys

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

template_letter_file = open(os.path.join(
    sys.path[0], "Input/Letters/starting_letter.txt"), mode="r")
letter_text = template_letter_file.read()

with open(os.path.join(sys.path[0], "Input/Names/invited_names.txt")) as names_file:
    for name in names_file.readlines():
        output_letter_file = open(os.path.join(
            sys.path[0], f"Output/ReadyToSend/ReadyToSendTo{name[:-1]}.txt"), mode="w")
        output_letter_file.write(letter_text.replace(
            "[name]", name[:-1]))
        output_letter_file.close()
