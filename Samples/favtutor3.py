def fizzbuzz(n):
    for i in range(1, n+1):
        output = ""
        output += "Fizz" * (i % 3 == 0)
        output += "Buzz" * (i % 5 == 0)
        print(output or str(i))

n = int(input("Enter a number: "))
fizzbuzz(n)
