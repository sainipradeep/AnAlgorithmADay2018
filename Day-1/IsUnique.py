# Day 1/365 #AnAlgorithmAday2018
# Problem is from Cracking the Coding Interview problem 1.1
# IS UNIQUE
#
# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
###############################################################################################################################


def isUnique(str1, str2):
    dict1 = {}
    dict2 = {}

    for item in str1:
        dict1[item] = dict1.get(item, 0) + 1

    for item in str2:
        dict2[item] = dict2.get(item, 0) + 1


    if dict1 == dict2:
        return True
    else:
        return False



isUnique("santa", "satan")

isUnique("fries", "friends")