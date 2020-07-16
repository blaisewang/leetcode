#
# @lc app=leetcode.cn id=298 lang=python3
#
# [298] 二叉树最长连续序列
#
# https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence/description/
#
# algorithms
# Medium (56.44%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    2.1K
# Total Submissions: 3.8K
# Testcase Example:  '[1,null,3,2,4,null,null,null,5]'
#
# 给你一棵指定的二叉树，请你计算它最长连续序列路径的长度。
# 
# 该路径，可以是从某个初始结点到树中任意结点，通过「父 - 子」关系连接而产生的任意路径。
# 
# 这个最长连续的路径，必须从父结点到子结点，反过来是不可以的。
# 
# 示例 1：
# 
# 输入:
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   / \
# ⁠  2   4
# ⁠       \
# ⁠        5
# 
# 输出: 3
# 
# 解析: 当中，最长连续序列是 3-4-5，所以返回结果为 3
# 
# 示例 2：
# 
# 输入:
# 
# ⁠  2
# ⁠   \
# ⁠    3
# ⁠   / 
# ⁠  2    
# ⁠ / 
# ⁠1
# 
# 输出: 2 
# 
# 解析: 当中，最长连续序列是 2-3。注意，不是 3-2-1，所以返回 2。
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
        def traverse(n: TreeNode, p: TreeNode, l: int) -> int:
            if n is None:
                return l

            l = l + 1 if p is not None and n.val == p.val + 1 else 1
            return max(l, max(traverse(n.left, n, l), traverse(n.right, n, l)))

        return traverse(root, None, 0)

# @lc code=end
