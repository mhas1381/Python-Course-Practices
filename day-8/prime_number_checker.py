def prime_checker(number):
    maghsoum=[]
    for numb in range(2 , number):
        if number %numb == 0:
            maghsoum.append(numb)
    print(maghsoum)
    if len(maghsoum)>2:
        print(f"{number} is not prime number")
    else:
        print(f"{number} is a prime number")




n = int(input("Enter a number to check it out it's prime or not: "))
prime_checker(number = n)