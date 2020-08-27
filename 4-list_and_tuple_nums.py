#!/usr/bin/env python

#Question 4
#Level 1

#Question:
#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

try:
    lst = input("Enter your list of numbers separated by a comma (no spaces): ").split(',')
    tup = tuple(lst)
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    print(lst)
    print(tup)
except ValueError:
    print("List must be of whole numbers.")