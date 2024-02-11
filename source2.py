import random

max_num = 500
min_num = 0

def printNumbers(start: int, finish: int) -> None:
    i = start
    while i < finish:
        print(i)
        i += 1

if __name__=="__main__":
    printNumbers(random.randint(min_num, min_num+10),
                 random.randint(min_num+11, max_num))
