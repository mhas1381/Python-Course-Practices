
age = input("What is your current age? ")
age_as_int = int(age)
age_remainig = 90 - age_as_int
days_left = age_remainig * 365
weeks_left = age_remainig * 52
month_left = age_remainig * 12

print(f'You have {days_left} days , {weeks_left} weeks and {month_left} months')