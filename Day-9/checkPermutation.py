# Day 9/365 #AnAlgorithmAday2018
# Problem is from Cracking the Coding Interview problem 1.2
# check permutation
#
# Given two strings, write a method to decide if one is a permutation of the other
###############################################################################################################################


def isPermutation(str1, str2):

    str1 = "".join(sorted(str1))

    str2 = "".join(sorted(str2))

    return str1 == str2