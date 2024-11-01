height = input("Enter your height in meter: ")
weight = input("Enter your weight in kilograms: ")

BMI = float(weight) / float(height)**2
print(f"your BMI is : {int(BMI)}")