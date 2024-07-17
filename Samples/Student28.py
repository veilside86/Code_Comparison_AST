possible_buzz = [5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80,
                 85, 95, 100]
# list of numbers that are replaced by Buzz

possible_fizz = [3, 6, 9, 12, 18, 21, 24, 27, 33,
                 36, 39, 42, 48, 51, 54, 57, 63, 66, 69,
                 72, 78, 81, 84, 87, 93, 96, 99]
# list of numbers replaced by Fizz

possible_fizz_buzz = [15, 30, 45, 60, 75, 90]
# list of numbers replaced by FizzBuzz

# for loop that tells the program what numbers to replace
for number in range(1, 101):
    if number in possible_buzz:
        print("Buzz")
    elif number in possible_fizz:
        print("Fizz")
    elif number in possible_fizz_buzz:
        print("FizzBuzz")
    else:
        print(number)
