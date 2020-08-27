#!/usr/bin/env python

#Question 8
#Level 2

#Question:
#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world

try:
    words = list(input("Please enter a list of words separated by commas: ").split(","))
    words.sort()
    for i in words:
        assert i.isalpha() #list items must be made of characters, not numbers
    print(*words, sep=",") #practice in unpacking lists/tuples, etc with the asterisk
   
except AssertionError:
    print("List must be of words.")