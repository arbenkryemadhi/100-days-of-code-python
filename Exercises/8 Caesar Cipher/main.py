from unittest import result
from art import logo

print(f"""
{logo}
Hello to Caesar Cipher. Made by Arben KRYEMADHI!
""")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

wants_to_continue = True


def caesar_cipher(plain_text, shift_amount, cipher_direction):
    text_type = ""

    if cipher_direction == "encode":
        text_type = "encoded"
    else:
        shift_amount = -shift_amount
        text_type = "decoded"

    refined_text = ""
    for letter in plain_text:
        if letter in alphabet:
            new_letter_index = alphabet.index(letter) + shift_amount
            if new_letter_index > 25:
                new_letter_index %= 26

            refined_text += alphabet[new_letter_index]
        else:
            refined_text += letter
    print(f"The {text_type} text is: {refined_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(plain_text=text, shift_amount=shift,
                  cipher_direction=direction)

    result = input("Do you want to continue? Yes or No? ").lower()
    if result == "no":
        should_continue = False
