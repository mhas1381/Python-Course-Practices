row1 = ["⬜" , "⬜" , "⬜"]
row2 = ["⬜" , "⬜" , "⬜"]
row3 = ["⬜" , "⬜" , "⬜"]
island_map = [row1 , row2 , row3]
print(f"{row1}\n{row2}\n{row3}\n")

user_choice = input("Where do you want put the tresure: ")
x = int(user_choice[0]) - 1
y = int(user_choice[1]) - 1
island_map[y][x] = "✅"
print(f"{row1}\n{row2}\n{row3}\n")
