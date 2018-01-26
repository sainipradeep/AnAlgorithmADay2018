# Day 24/365 #AnAlgorithmAday2018
# Problem is from Leetcode 100
#
# Same Tree
#
#GGiven two binary trees, write a function to check if they are the same or not.
#
#Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
#
#Example 1:
#
#Input:     1         1
#          / \       / \
#         2   3     2   3
#
#       [1,2,3],   [1,2,3]
#
#Output: true
#Example 2:
#
#Input:     1         1
#          /           \
#         2             2
#
#        [1,2],     [1,null,2]
#
#Output: false
#Example 3:
#
#Input:     1         1
#          / \       / \
#         2   1     1   2
#
#        [1,2,1],   [1,1,2]
#
#Output: false
########################################################################################################################


class TreeNode(object):
    def __init__(self, x):
        self.val = x:
        self.right = None
        self.left = None


class Solution(object):
    def isSameTree(self, tree1, tree2):
        if tree1 and tree2:
            return tree1.val == tree2.val and self.isSameTree(tree1.left, tree2.left) and self.isSameTree(tree1.right, tree2.right)

        return tree1 is tree2

