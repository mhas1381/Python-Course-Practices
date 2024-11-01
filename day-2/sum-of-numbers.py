number = input("Enter a number: ")

# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
#
# result = first_digit + second_digit
# print(result)
#
sum = 0
for n in number:
    sum += int(n)

print(sum)