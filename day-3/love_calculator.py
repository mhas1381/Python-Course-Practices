print("Welcome to Love Calculator app!")
name1 = input("Enter your name : ").lower()
name2 = input("Enter your crush name : ").lower()
whole_name = name1 + name2

TRUE = str(whole_name.count("t") + whole_name.count("r") + whole_name.count("u") + whole_name.count("e"))
LOVE = str(whole_name.count("l") + whole_name.count("o") + whole_name.count("v") + whole_name.count("e"))

score = int(TRUE + LOVE)

if score >=90 or score <= 10:
    print(f"Your score is {score} , you together like coke and mentos.")
elif 40 <= score <=50 :
    print(f"Your score is {score} , you are alright together")
else:
    print(f"Your score is {score}")