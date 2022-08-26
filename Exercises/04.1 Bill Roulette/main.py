import random

print("Welcome to \"Bill Roulette\"")
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_name_index = random.randint(0, len(names)-1)
print(f"{names[random_name_index]} is going to buy the meal today!")
