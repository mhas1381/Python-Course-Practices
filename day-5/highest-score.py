scores = input("Enter scores:\n").split()

for score in range(0 , len(scores)):
    scores[score] = int(scores[score])

highest_score = 0
# for score in range(len(scores)):
#     if scores[score] > scores[score - 1]:
#         highest_score = scores[score]
for score in scores:
    if score > highest_score:
        highest_score = score
print(f"highest_score is {highest_score}")