def fizz_buzz(n):
    """
    Function to print numbers from 1 to n with specific replacements for multiples of 3 and 5.

    Parameters:
    - n: int
        The upper limit until which numbers will be printed.

    Returns:
    - None
        This function does not return anything, it just prints the numbers or replacements.

    Example:
    - fizz_buzz(15)
        This will print the following:
        1
        2
        Fizz
        4
        Buzz
        Fizz
        7
        8
        Fizz
        Buzz
        11
        Fizz
        13
        14
        FizzBuzz
    """

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example of using the fizz_buzz function:

# Printing numbers from 1 to 20 with FizzBuzz replacements
fizz_buzz(20)
