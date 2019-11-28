#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (40.57%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    38.9K
# Total Submissions: 95.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最小深度  2.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        if not root.left:
            return self.minDepth(root.right) + 1

        if not root.right:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        # if not root:
        #     return 0
        #
        # q = deque([(1, root)])
        #
        # while q:
        #
        #     depth, node = q.popleft()
        #
        #     if not node.left and not node.right:
        #         return depth
        #
        #     if node.left:
        #         q.append((depth + 1, node.left))
        #     if node.right:
        #         q.append((depth + 1, node.right))

# @lc code=end
