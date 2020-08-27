#!/usr/bin/env python

#Question 6
#Level 2

#Question:
#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.
#Example
#Let us assume the following comma separated input sequence is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24
#If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
#In case of input data being supplied to the question, it should be assumed to be a console input. 

from math import sqrt
# C and H are constants
C = 50
H = 30

try:
    lst = list((input("Please enter a list of values (or just one) to determine their Q (separated by commas, no spaces): ")).split(","))
    for i in range(len(lst)):
        lst[i] = float(lst[i])
    for D in lst:
        #formula for Q rounded to the nearest whole number
        Q = round(sqrt((2 * C * D) / H))
        if D != lst[-1]:
            print(Q, end=", ")
        else: #makes sure the last one in the list does not have a comma trailing after it
            print(Q)
except ValueError:
    print("You must enter a list of numbers.")

input("Press any key to exit: ") #If running just the program from a file, this ensures the window stays open until you want it to close
