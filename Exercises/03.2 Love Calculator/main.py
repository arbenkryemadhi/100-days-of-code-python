print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Add both names together in order to make counting letters in each eaisier
both_names = name1.lower() + name2.lower()

# Counting "true love" for each letter
t_count = both_names.count("t")
r_count = both_names.count("r")
u_count = both_names.count("u")
e_count = both_names.count("e")
l_count = both_names.count("l")
o_count = both_names.count("o")
v_count = both_names.count("v")

# Works XY score by making 1st number X by multiplying by 10
number1 = (t_count + r_count + u_count + e_count) * 10
number2 = l_count + o_count + v_count + e_count
score = number1 + number2

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
