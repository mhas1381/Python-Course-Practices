height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

BMI = round(weight / height ** 2, 2)

if BMI < 18.5:
    status = "underweight"
elif BMI < 25:
    status = "normal weight"
elif BMI < 30:
    status = "overweight"
elif BMI < 35:
    status = "obese"
else:
    status = "clinically obese"

print(f"Your BMI is {BMI} , you are {status}")
