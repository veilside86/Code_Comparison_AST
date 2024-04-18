# A for loop can be used to evaluate all the numbers between 1 and 100, using "number" as a variable.
for number in range(1, 101):
    # We need multiples of 3 and 5 to print "FizzBuzz". We can do that by setting "15" as our range interval.
    # It's also important that this is the stated first in our conditions, otherwise "Fizz" and/or "Buzz" would override
    # our "FizzBuzz" values.
    if number in range(0, 101, 15):
        print("FizzBuzz")
    # We'll use a very similar flow to printout "Fizz" for multiples of 3 and "Buzz" for multiples of 5.
    elif number in range(0, 101, 3):
        print("Fizz")
    elif number in range(0, 101, 5):
        print("Buzz")
    # All other numbers need to print themselves, no strings needed. Therefore, we print the variable "number".
    else:
        print(number)
