# First Way

for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Second Way

for number in range(1, 101):
    __message = ""

    if number % 3 == 0:
        __message += "Fizz"
    if number % 5 == 0:
        __message += "Buzz"
    if number % 3 != 0 and number % 5 != 0:
        __message += str(number)

    print(__message)
