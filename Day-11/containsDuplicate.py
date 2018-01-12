# Day 11/365 #AnAlgorithmAday2018
# Problem is from Leetcode 217
#
# Contains Duplicate
#
#Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least #twice in the array, and it should return false if every element is distinct.
#
#
########################################################################################################################

def containsDuplicate(nums):
    if not nums:
        return False
            
    values = {}
            
    for item in nums:
        values[item] = values.get(item, 0) + 1
        
        
    for key, value in values.iteritems():
        if value >= 2:
            return True
        
        
    return False
