students_heights = input("Enter heights:\n").split()

for height in range(0 , len(students_heights)):
    students_heights[height] = int(students_heights[height])
# print(students_heights)

sum = 0
count = 0
for height in students_heights:
    sum += height
    count += 1

average = round(sum/count)
print(average)