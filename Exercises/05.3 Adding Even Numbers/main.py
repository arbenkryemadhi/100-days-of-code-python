upper_number = int(input("Up to wich number do you want to add all evens?\n"))

sum = 0

for number in range(0, upper_number + 1, 2):
    sum += number
print(sum)
