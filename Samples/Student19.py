#Quiz #6
#multiples of three fizz
#multiples of five buzz
#multiple of both five and three fizzbuzz

number = range(1-100)
multiple_of_3= f"fizz"
multiple_of_5= f"buzz"
multiple_of_3_5= f"fizzbuzz"


for l in range(1, 100):
    if l % 3 == 0:
        print(str("fizz"))
    elif l % 5 == 0:
        print(str("buzz"))
    elif l % 5 % 3 == 0:
        print((str("fizzbuzz")))
    else:
        print(str(l))