#Question 2
#Level 1

#!/usr/bin/env python

#Question:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

#This answer includes an error if the user puts in something that is not an integer. 
try:
    num1 = int(input("Please enter the number to compute the factorial: "))
    def factorial(num1):
        fact = 1
        count = num1
        while count > 0:
            fact *= count
            count -= 1
        print(fact)
    factorial(num1)
except ValueError:
    print("You must enter a whole number.")