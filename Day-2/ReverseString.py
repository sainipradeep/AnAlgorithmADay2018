# Day 2/365 #AnAlgorithmAday2018
# Problem is from Leetcode 344
# Reverse String
#
# Write a function that takes a string as input and returns the string reversed.
#
#Example:
#Given s = "hello", return "olleh".
###############################################################################################################################

def reverseString(str):
    reversedStr = ""

    for char in str:
        reversedStr = char + reversedStr

    return reversedStr

    
