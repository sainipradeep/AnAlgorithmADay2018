# Day 8/365 #AnAlgorithmAday2018
# Problem is from Leetcode 20
#
# Valid Parentheses
#
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
########################################################################################################################

def validParentheses(str):

    stack = []

    valueKeyDict = {']':'[', '}':"{", ')':"("}

    for item in str:
        if item in valueKeyDict.values():
            stack.append(item)
        elif item in valueKeyDict.keys():
            if stack == [] or valueKeyDict[item] != stack.pop():
                return False
        else:
            return False


    return stack == []
