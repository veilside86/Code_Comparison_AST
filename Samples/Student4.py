
for numbs in range(100):
    if numbs % 3 == 0 and numbs % 5 == 0:
        print("fizzbuzz")
        continue
    elif numbs % 3 == 0:
        print("fizz")
        continue
    elif numbs % 5 == 0:
        print("buzz")
        continue
    print(numbs)