#
# @lc app=leetcode.cn id=1120 lang=python3
#
# [1120] 子树的最大平均值
#
# https://leetcode-cn.com/problems/maximum-average-subtree/description/
#
# algorithms
# Medium (58.89%)
# Likes:    27
# Dislikes: 0
# Total Accepted:    1.8K
# Total Submissions: 3.1K
# Testcase Example:  '[5,6,1]'
#
# 给你一棵二叉树的根节点 root，找出这棵树的 每一棵 子树的 平均值 中的 最大 值。
# 
# 子树是树中的任意节点和它的所有后代构成的集合。
# 
# 树的平均值是树中节点值的总和除以节点数。
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：[5,6,1]
# 输出：6.00000
# 解释： 
# 以 value = 5 的节点作为子树的根节点，得到的平均值为 (5 + 6 + 1) / 3 = 4。
# 以 value = 6 的节点作为子树的根节点，得到的平均值为 6 / 1 = 6。
# 以 value = 1 的节点作为子树的根节点，得到的平均值为 1 / 1 = 1。
# 所以答案取最大值 6。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数介于 1 到 5000之间。
# 每个节点的值介于 0 到 100000 之间。
# 如果结果与标准答案的误差不超过 10^-5，那么该结果将被视为正确答案。
# 
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
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        r = float("-inf")

        def traverse(node: TreeNode):
            nonlocal r
            if not node:
                return 0, 0

            ls, lc = traverse(node.left)
            rs, rc = traverse(node.right)
            cs = ls + rs + node.val
            cc = lc + rc + 1
            r = max(r, cs / cc)

            return cs, cc

        traverse(root)
        return r

# @lc code=end
