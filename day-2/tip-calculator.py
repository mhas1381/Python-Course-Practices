print("Welcome to tip calculator!")
total_bill = float(input("What was the total bill ? $"))
percentage = float(input("What percentage tip would you like to give ? 10,12 or 15 ? "))
persons_count = int(input("How many peaple to split the bill? "))


qouta = round((total_bill / persons_count) * (1 + percentage/100),2)
print(f'Each person should pay ${qouta}')