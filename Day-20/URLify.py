# Day 20/365 #AnAlgorithmAday2018
# Problem is from CTCI 1.3emove Elements
#
#Write a method to replaxce all spaces in a string with a string '%20'. you are given the true length of the string
#
#"mr john smith", 13  => mr%20john%20smith
########################################################################################################################


def URLify(str1, length):

    str1 = str1[:length]

    return str1.replace(' ', '%20')