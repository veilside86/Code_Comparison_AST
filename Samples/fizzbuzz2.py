#FizzBuzz Program
def main():
    for num in range(1, 100):
        if (num%3==0 and num%5==0):
            print("Fizz Buzz")
        elif (num%5==0):
            print("Buzz")
        elif (num%3==0):
            print("Fizz")
        else:
            print(num)


main()