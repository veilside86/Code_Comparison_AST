#this is the FizZ/Buzz part
#make this into a for loop in order to repeat many times
for num in range(0, 101):
    # if the remainder is 0 then that means that the number goes into the other number
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 + num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)

