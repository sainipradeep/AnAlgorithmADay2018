# Day 22/365 #AnAlgorithmAday2018
# Problem is from Leetcode 257
#
# Binary Tree Paths
#
#Given a binary tree, return all root to leaf paths
#
#Example
#For example, given the following binary tree:
#
#   1
# /   \
#2     3
# \
#  5
#All root-to-leaf paths are:
#
#["1->2->5", "1->3"]
#
########################################################################################################################


class TreeNode(object):
    def __init__(self, x):
        self.x = val
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):

        if root is None:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        result = []

        if root.left:
            result = self.binaryTreePaths(root.left)
            result = [str(root.val) + "->" + x for x in result]

        if root.right:
            result = self.binaryTreePaths(root.right)
            result = [str(root.val) + "->" + x for x in temp]
            result += temo

        return result