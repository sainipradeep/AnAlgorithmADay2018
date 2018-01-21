# Day 19/365 #AnAlgorithmAday2018
# Problem is from Leetcode 141
#
# Linked List Cycle
#
#Given a linked list, determine if it has a cycle in it
#
#
########################################################################################################################

class ListNode(object):
    def __init__(self, x):
        self.x = val
        self.next = None


class Solution(object):
    def linkedListCycle(self, head):

        try:
            current = head
            pointer = head.next

            while current is not pointer:
                current = current.next
                pointer = pointer.next.next

            return True

        except:
            return False