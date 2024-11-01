print("Welcome to leap year detector app!")

year = int(input("Enter year to check it out : "))


if year % 100 == 0 :
    if year % 400 == 0:
        print("leap year")
    else:
        print("not leap year")
elif year % 4 == 0:
    print("leap year")
else:
    print("not leap year")