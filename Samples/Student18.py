fizz_divisor = 3
buzz_divisor = 5
for num in range(1, 101):
    if (num % fizz_divisor == 0) and (num % buzz_divisor == 0):
        print("FizzBuzz")
    elif (num % fizz_divisor == 0):
        print("Fizz")
    elif (num % buzz_divisor == 0):
        print("Buzz")
    else:
        print(num)
