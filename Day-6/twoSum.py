# Day 6/365 #AnAlgorithmAday2018
# Problem is from Leetcode 1
#
# Two sum
#
#Given an array of integers, return indices of the two numbers such that they add up to a specific target
#You may assume that each input would have exactly one solution and you may not use the same element twice
#
#Given nums =[2, 7, 11, 15],  target=9
#Because nums[0] + nums[1] = 2 + 7 = 9
#return [0,1]
########################################################################################################################

def twoSum(nums, target):

    dict_sums = {}

    for n, num in enumerate(nums):
        if num in dict_sums:
            return [dict_sums[num], n]
        dict_sums[target - num] = n

        
