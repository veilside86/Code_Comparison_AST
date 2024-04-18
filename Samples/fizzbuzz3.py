#Ahmad Somakia
#Pal session project


def main():
    numbers = range(1,101)
# I had trouble getting the range to start from 1 and end at 100, so it won't include 0 since I am using remainders to find multiples of
    # 3 and 5 and the remainder of 0/3 and 0/5 is always 0 and so it would actually include the number 100 in the operation.
    # then I realized expanding the range from 1,101 excludes 0 and includes 100.
    for number in numbers :
        threes = number % 3
        fives = number % 5
        fifteens = number % 15
        if fifteens == 0:
            print("FizzBuzz")
            # I had to put the divisible by 3 and 5 first because it was printing fizz when I used the elif.

        elif threes == 0 :
            print("Fizz")
        elif fives == 0 :
            print("Buzz")
            # I had 3 seperate if statements but I turned them into elif statements to include all the requirements.
        else:
            print(number)
main()

# the end.