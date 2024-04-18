def fizz_buzz(n):
    mappings = {3: 'Fizz', 5: 'Buzz'}
    for i in range(1, n+1):
        output = ''
        for key in mappings:
            if i % key == 0:
                output += mappings[key]
        if not output:
            output = i
        print(output)

# Test the function with n = 15
fizz_buzz(15)
