
#used to check for multiples of 3 and 5 and print those accordingly
def main():
    for number in range(1, 100):
        if number%3 and number%5 ==0:
            print("FizzBuzz")
        elif number%3 ==0:
            print("Fizz")
        elif number%5 ==0:
            print("Buzz")
        else:
            print(number)

main()