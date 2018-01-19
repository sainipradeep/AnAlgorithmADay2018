# Day 18/365 #AnAlgorithmAday2018
# Problem is from Leetcode 83
#
# reverse a linkedlist
#
#Given a sorted linked list, delete all duplicates such that each element appear only once.
#
#For example,
#Given 1->1->2, return 1->2.
#Given 1->1->2->3->3, return 1->2->3.
########################################################################################################################

class ListNode(object):
    def __init__(self, n):
        self.val = n
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):

        curr = head

        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next == curr.next.next

            curr = curr.next

        return head
