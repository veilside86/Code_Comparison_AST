def fizzbuzz(n):
    mappings = {3: 'Fizz', 5: 'Buzz'}
    for i in range(1, n+1):
        output = ''.join([value for key, value in mappings.items() if i % key == 0])
        print(output or str(i))

n = int(input("Enter a number: "))
fizzbuzz(n)
