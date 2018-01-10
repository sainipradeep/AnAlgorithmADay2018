# Day 10/365 #AnAlgorithmAday2018
# Problem is from Leetcode 136
#
# Single Number
#
#Given an array of integers, every element appears twice except for one. Find that single one.

#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
########################################################################################################################

def singleNumber(lst):

    dict_values ={}

    for item in lst:
        dict_values[item] = dict_values.get(item, 0) + 1


    for key, value in dict_values.iteritems():
        if value == 1:
            return key


    return 0