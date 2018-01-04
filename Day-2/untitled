# Day 3/365 #AnAlgorithmAday2018
# Problem is from Leetcode 136
# Single Number
#
# Given an array of integers, every element appears twice except for one. Find that single one.
###############################################################################################################################

def singleNumber(nums):

    nums_dict = {}

    for item in nums:
        nums_dict[item] = nums_dict.get(item, 0) + 1


    for key, value in nums_dict.iteritems():
        if value == 1:
            return key


    return False
