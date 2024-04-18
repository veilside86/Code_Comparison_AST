def fizz_buzz(n):
    """
    Prints numbers from 1 to n with specific rules:
    - For multiples of 3, prints 'Fizz'.
    - For multiples of 5, prints 'Buzz'.
    - For multiples of both 3 and 5, prints 'FizzBuzz'.

    Parameters:
    - n (int): The upper limit of numbers to print.

    Returns:
    None

    Examples:
    - fizz_buzz(5) will output:
      1
      2
      Fizz
      4
      Buzz

    - fizz_buzz(15) will output:
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
        # Checking for multiples of both 3 and 5 first
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # Checking for multiples of 3
        elif i % 3 == 0:
            print("Fizz")
        # Checking for multiples of 5
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example of using the fizz_buzz function:
fizz_buzz(20)
