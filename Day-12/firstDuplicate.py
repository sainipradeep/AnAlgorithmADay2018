# Day 12/365 #AnAlgorithmAday2018
# Problem is from Codefights
#
#First Duplicate
#
#Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for 
#which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, 
#return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. 
#If there are no such elements, return -1.
#
#
########################################################################################################################


def firstDuplicate(lst):

    seen = set()

    for item in lst:
        if item in seen:
            return item

        seen.add(item)


    return -1