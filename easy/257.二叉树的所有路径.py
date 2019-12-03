#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (60.70%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    19.4K
# Total Submissions: 31.9K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 输入:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        if not root:
            return []

        r = []
        s = [(root, str(root.val))]
        while s:
            node, path = s.pop()
            if not node.left and not node.right:
                r.append(path)
            if node.left:
                s.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                s.append((node.right, path + "->" + str(node.right.val)))

        return r

# @lc code=end
