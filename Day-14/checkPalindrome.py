# Day 14/365 #AnAlgorithmAday2018
# Problem is from Codefights
#
# check palindrome
#
#For inputString = "aabaa", the output should be
#checkPalindrome(inputString) = true;
#For inputString = "abac", the output should be
#checkPalindrome(inputString) = false;
#For inputString = "a", the output should be
#checkPalindrome(inputString) = true.

########################################################################################################################


def checkPalindrome(str1):

    return str1 == str1[::-1]

