#!/usr/bin/env python

#Question 7
#Level 2

#Question:
#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1.
#Example
#Suppose the following inputs are given to the program:
#3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

try:
    lst = list(input("Please enter X and Y as whole numbers separated by a comma (no spaces): " ).split(","))
    x = int(lst[0])
    y = int(lst[1])
    def twod_array(x, y):
        array = [[i*j for i in range(y)]for j in range(x)] #good list comprehension practice
        print(array)
    twod_array(x, y)
except ValueError:
    print("X and Y must be whole numbers.")