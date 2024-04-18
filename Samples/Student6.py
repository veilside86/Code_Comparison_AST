#Dominic Di Giacomo
for num in range(1,100,1):
    if num % 5 == 0 and num % 3 != 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)