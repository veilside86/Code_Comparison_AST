for num in range(1,101,1):
    print(f"{num}")

if num == '3' or '6' or '9' or '12' or '18' or '21' or '24' or '27' or '33' or '36' or '39' or '42' or '48' or '51' or '54' or '57' or '63' or '66' or '69' or '72' or '78' or '81' or '84' or '87' or '93' or '96' or '99':
    print(f"Fizz")
if num /5:
    print(f"Buzz")
if num /15:
    print(f"FizzBuzz")

#trying to use if for each because i think it'll allow if the number is divisable by both
#3 and 5 it'll overwrite the two commands before


#what I want to do it make it print a range of 1 to 100 and have the program
#replace every number divisable by 3 with Fizz and /5 replaced with Buzz, accept
#when it's a multiple of 15, which will be replaced with FizzBuzz
#the only issue being i don't know how