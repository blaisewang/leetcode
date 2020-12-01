#
# @lc app=leetcode.cn id=1666 lang=python3
#
# [1666] Change the Root of a Binary Tree
#
# https://leetcode-cn.com/problems/flip-binary-tree/description/
#
# algorithms
# Medium (82.14%)
# Likes:    0
# Dislikes: 0
# Total Accepted:    27
# Total Submissions: 36
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n7'
#
# Given the root of a binary tree and a leaf node, reroot the tree so that the
# leaf is the new root.
# 
# You can reroot the tree with the following steps for each node cur on the
# path starting from the leaf up to the root​​​ excluding the root:
# 
# 
# If cur has a left child, then that child becomes cur's right child. Note that
# it is guaranteed that cur will have at most one child.
# cur's original parent becomes cur's left child.
# 
# 
# Return the new root of the rerooted tree.
# 
# Note: Ensure that your solution sets the Node.parent pointers correctly after
# rerooting or you will receive "Wrong Answer".
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 7
# Output: [7,2,null,5,4,3,6,null,null,null,1,null,null,0,8]
# 
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 0
# Output: [0,1,null,3,8,5,null,null,null,6,2,null,null,7,4]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [2, 100].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# leaf exist in the tree.
# 
# 
#


# @lc code=start
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def flipBinaryTree(self, root: Node, leaf: Node) -> Node:
        if root is leaf:
            return root

        node = leaf
        leaf.left, leaf.parent = leaf.parent, None
        while node.left is not root:
            if node.left.right is node:
                node.left.right = node.left.left

            node.left.left = node.left.parent
            node.left.parent = node
            node = node.left

        if node.left.left is node:
            node.left.left = None
        else:
            node.left.right = None

        node.left.parent = node

        return leaf

# @lc code=end
