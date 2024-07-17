for number in range (1,101):
    print(f"Count with me!: {number}")
number = input("start counting")
if int(number) <3:
    print("fizz")
elif int(number) ==5:
    print("buzz")
elif int(number) ==3 or 5:
    print("fizzbuzz")
else:
    print(f"number: {number}")

