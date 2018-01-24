# Day 23/365 #AnAlgorithmAday2018
# Problem is from Leetcode 404
#
# Sum of left leaves
#
#Given a binary tree, find the sum of all left leaves
#
#  3
#   / \
#  9  20
#    /  \
#   15   7
#
#There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
########################################################################################################################

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):

        if not root:
            return 0

        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)



