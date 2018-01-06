# Day 5/365 #AnAlgorithmAday2018
# Problem is from Leetcode 485
#
# Max Consecutive Ones
#
#Given a binary array, find the maximum number of consecutive 1s in this array
#
#
#[1,1,0,1,1,1]   answer is 3
########################################################################################################################

def maxConsecutiveOnes(lst):
    highest = 0
    count = 0

    for item in lst:
        if item == 1:
            count += 1
        else:
           highest = max(highest, count)
           count = 0


    return max(highest, count)


    

