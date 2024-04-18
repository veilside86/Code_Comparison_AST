# Course: COMP151
# Project: hw04
#  Program Purpose: Write a program to prompt for the number of triangles and the height of each triangle, then print out all the specified triangles.
# Date: 10/17/2017
# Author: CHIHO HAN

t = eval(input("How many triangles: "))        # Input: how many triangles print
print("")
for i in range(t):           # loop statement for triangles
    s = 1                       # the number starts from 1
    h = eval(input("The height of the triangles: "))           # Input the height of triangle
    for j in range (h):             # loop for each row
        for k in range(h-j):            # loop for columns
            print(s, end = "\t")                # Output: numbers
            s += 2          # add 2 for printing odd numbers
        print()           # turning to next raw
