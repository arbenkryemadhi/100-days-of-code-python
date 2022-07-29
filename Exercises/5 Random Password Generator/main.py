import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# Choses a letter which corresponds to a randomly generated index and adds it to the string.
pw_letters = ""
for x in range(0, nr_letters):
    pw_letters += random.choice(letters)

pw_numbers = ""
for x in range(0, nr_numbers):
    pw_numbers += random.choice(numbers)

pw_symbols = ""
for x in range(0, nr_symbols):
    pw_symbols += random.choice(symbols)

password = pw_letters + pw_numbers + pw_symbols

shuffled_pw = ""
random_index = 0

for x in range(0, len(password)):
    # Choses the index of the letter that will be first on the new string: "abc"[2] = "c"
    random_index = random.randint(0, len(password)-1)
    # Adds teh letter to the new shuffled pw
    shuffled_pw += password[random_index]
    # Keeps every char up to the index, keeps everything after index
    password = password[:random_index] + password[(random_index+1):]

print(shuffled_pw)
