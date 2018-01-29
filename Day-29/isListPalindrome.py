# Day 29/365 #AnAlgorithmAday2018
# Problem is from codefights
#
# linked list palindrome
#
#
#Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l, since this is what you'll be asked #to do during an interview.
#
#Given a singly linked list of integers, determine whether or not it's a palindrome.
#
#Example
#
#For l = [0, 1, 0], the output should be
#isListPalindrome(l) = true;
#For l = [1, 2, 2, 3], the output should be
#isListPalindrome(l) = false.
########################################################################################################################



# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    
    if not l:
        return True

    head = l
    prev = None
    while l.next:
        l.prev = prev
        prev = l
        l = l.next
    tail = l
    tail.prev = prev
    while head is not tail and head.value == tail.value:
        head = head.next
        tail = tail.prev
    if head is tail:
        return True
    elif head.value == tail.value:
        return True
    else:
        return False
