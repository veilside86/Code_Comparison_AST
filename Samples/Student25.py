for number in range(1, 101, 1):
    # In this first if I want the program to print "FizzBuzz if the remainder of the number == 0 in both cases
    if int(number % 3) == 0 and int(number % 5) == 0:
        print("FizzBuzz")
#  In this elif I want the program to print Fizz if the number's remainder divided by 3 == 0
    elif int(number % 3) == 0:
        print("Fizz")
# Print buzz if the remainder == 0 (same process as before)
    elif int(number % 5) == 0:
        print("Buzz")
# if it doesn't fulfill any of the statements just print the number by itself.
    else:
        print(number)
