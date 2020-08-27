#!/usr/bin/env python

#Question 5
#Level 1

#Question:
#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class Test:
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = input("Please enter a string: ")
    def printString(self):
        print(self.string.upper())

#init instance of class Test
a = Test()
#tests printString when getString has not been done (default string is an empty string)
a.printString()
#tests getString to get the string from user input and store in self.string
a.getString()
#tests printing the string gotten from getString
a.printString()

