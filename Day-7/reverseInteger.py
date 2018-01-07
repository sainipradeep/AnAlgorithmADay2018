# Day 7/365 #AnAlgorithmAday2018
# Problem is from Leetcode 7
#
# Reverse Integer
#
#Given a 32-bit signed integer, reverse digits of an integer
# 123 ==> 321
#-123 ==> -321
########################################################################################################################


def reverseInteger(num):

    if num >= 0:
        result = int(str(num)[::-1])

    else:
        result = int('-' + str(num)[:0:-1])


    return result