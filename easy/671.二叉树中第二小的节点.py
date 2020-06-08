#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#
# https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (44.74%)
# Likes:    79
# Dislikes: 0
# Total Accepted:    11.9K
# Total Submissions: 25.6K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或
# 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。 
# 
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
# 
# 示例 1:
# 
# 
# 输入: 
# ⁠   2
# ⁠  / \
# ⁠ 2   5
# ⁠    / \
# ⁠   5   7
# 
# 输出: 5
# 说明: 最小的值是 2 ，第二小的值是 5 。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# ⁠   2
# ⁠  / \
# ⁠ 2   2
# 
# 输出: -1
# 说明: 最小的值是 2, 但是不存在第二小的值。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
import heapq


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        h = [-float('inf'), -float('inf')]

        def f(r):
            if r:
                -r.val not in h and heapq.heappushpop(h, -r.val)
                f(r.left)
                f(r.right)

        f(root)
        return h[0] == -float('inf') and -1 or -h[0]

# @lc code=end
