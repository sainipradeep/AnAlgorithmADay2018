# Day 27/365 #AnAlgorithmAday2018
# Problem is from Leetcode 101
#
# Symmetric Tree
#
#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
#For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#    1
#   / \
#  2   2
# / \ / \
#3  4 4  3
#But the following [1,2,2,null,3,null,3] is not:
#    1
#   / \
#  2   2
#   \   \
#   3    3
#Note:
#Bonus points if you could solve it both recursively and iteratively.
#
#
########################################################################################################################

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):


        def sym_tree(L,R):
            if L and R:
                return L.val == R.val and sym_tree(L.left, R.right) and sym_tree(L.right, R.left)
            else:
                return L == R

        return sym_tree(root, root)





