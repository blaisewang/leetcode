#
# @lc app=leetcode.cn id=549 lang=python3
#
# [549] 二叉树中最长的连续序列
#
# https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence-ii/description/
#
# algorithms
# Medium (50.25%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    1.1K
# Total Submissions: 2.1K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个二叉树，你需要找出二叉树中最长的连续序列路径的长度。
# 
# 请注意，该路径可以是递增的或者是递减。例如，[1,2,3,4] 和 [4,3,2,1] 都被认为是合法的，而路径 [1,2,4,3]
# 则不合法。另一方面，路径可以是 子-父-子 顺序，并不一定是 父-子 顺序。
# 
# 示例 1:
# 
# 输入:
# ⁠       1
# ⁠      / \
# ⁠     2   3
# 输出: 2
# 解释: 最长的连续路径是 [1, 2] 或者 [2, 1]。
# 
# 
# 
# 
# 示例 2:
# 
# 输入:
# ⁠       2
# ⁠      / \
# ⁠     1   3
# 输出: 3
# 解释: 最长的连续路径是 [1, 2, 3] 或者 [3, 2, 1]。
# 
# 
# 
# 
# 注意: 树上所有节点的值都在 [-1e7, 1e7] 范围内。
# 
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 1

        def traverse(node: TreeNode):
            nonlocal res

            if not node:
                return 0, 0
            l, r = traverse(node.left), traverse(node.right)
            i, d = 1, 1
            if node.left:
                if node.left.val == node.val + 1:
                    i += l[0]
                elif node.left.val == node.val - 1:
                    d += l[1]
            if node.right:
                if node.right.val == node.val + 1:
                    i = max(i, r[0] + 1)
                elif node.right.val == node.val - 1:
                    d = max(d, r[1] + 1)

            res = max(res, i + d - 1)
            return i, d

        traverse(root)
        return res

# @lc code=end
