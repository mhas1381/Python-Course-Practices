import math
def paint_calc(height , weight , cover):
    number_of_cans = math.ceil(( height * weight ) / cover)
    print(number_of_cans)

test_h = int(input("Height of wall: "))
test_w = int(input("weight of wall: "))
coverage = 5
paint_calc(height = test_h , weight = test_w , cover=coverage)