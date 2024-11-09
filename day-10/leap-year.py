print("Welcome to leap year detector app!")


def is_leap():
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


def day_in_month(year, month):
    if month > 12 and month < 1:
        return "Invalid input"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month]


year = int(input("Enter a year to check it out : "))
month = int(input("Enter a month : "))
days = day_in_month(year, month)
print(days)
