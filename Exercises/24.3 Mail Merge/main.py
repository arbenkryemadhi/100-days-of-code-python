import os
from os import sys

with open(os.path.join(
        sys.path[0], "Input/Letters/starting_letter.txt"), mode="r") as template_letter_file:
    letter_text = template_letter_file.read()

with open(os.path.join(sys.path[0], "Input/Names/invited_names.txt")) as names_file:
    for name in names_file.readlines():
        output_letter_file = open(os.path.join(
            sys.path[0], f"Output/ReadyToSend/ReadyToSendTo{name[:-1]}.txt"), mode="w")
        output_letter_file.write(letter_text.replace(
            "[name]", name[:-1]))
        output_letter_file.close()
