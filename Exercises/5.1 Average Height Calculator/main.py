student_heights = input("Input a list of student heights:\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

number_of_heights = 0
hights_sum = 0
average_hight = 0

for i in student_heights:
    number_of_heights += 1

for i in student_heights:
    hights_sum += i

average_hight = round(hights_sum / number_of_heights)
print(f"Average height is: {average_hight}")
