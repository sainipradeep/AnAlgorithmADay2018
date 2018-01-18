# Day 17/365 #AnAlgorithmAday2018
# Problem is from Leetcode 203
#
# Remove Elements
#
#Remove all elements from a linked list of integers that have value val.
#
#Example
#Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
#Return: 1 --> 2 --> 3 --> 4 --> 5
#
#
########################################################################################################################

class Node(object):
    def __init__(self, n):
        self.val = n:
        self.next = None

class Solution(object):
    def removeElements(self, head, val):

        while head is not None and head.val == val:
            head = head.next

        if head is None:
            return None

        curr = head

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head