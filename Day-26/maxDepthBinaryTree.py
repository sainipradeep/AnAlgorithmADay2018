# Day 26/365 #AnAlgorithmAday2018
# Problem is from Leetcode 104
#
# Maximum Depth of Binary Tree
#
#Given a binary tree, find its maximum depth.
#
#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
#
#
########################################################################################################################

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepthBinaryTree(self, root):

        if not root:
            return 0

        left_depth, right_depth = self.maxDepthBinaryTree(root.left), self.maxDepthBinaryTree(root.right)

        if left_depth >= right_depth:
            return left_depth + 1

        else:
            return right_depth + 1
