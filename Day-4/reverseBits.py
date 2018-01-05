# Day 4/365 #AnAlgorithmAday2018
# Problem is from Leetcode 190
#
# Reverse bits of a given 32 bits unsigned integer.
#
#For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as #00111001011110000010100101000000).
#
#Follow up:
#If this function is called many times, how would you optimize it?
########################################################################################################################



def reverseBits(n):

    binary = '{0:032b}'.format(n)

    rev = ""

    for item in binary:
        rev = item + rev

    return int(rev, 2)