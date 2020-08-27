#!/usr/bin/env python

#Question:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

#I did one better. I made a program that will ask for input on what the user wants the range to be. 
try:
    print("This is a program that will tell you the numbers in a range that are divisible by 7 but are not a multiple of 5.")
    num1 = int(input("What is the first (whole) number in the range: "))
    num2 = int(input("What is the second (whole) number in the range (inclusive): "))
    def q1(num1, num2):
        for i in range(num1, num2+1):
            if i % 7 == 0 and i % 5 != 0:
                print(i, end=", ")

    q1(num1, num2)
except ValueError:
    print("Numbers in the range must be whole numbers.")
