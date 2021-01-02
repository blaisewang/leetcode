#
# @lc app=leetcode.cn id=270 lang=python3
#
# [270] 最接近的二叉搜索树值
#
# https://leetcode-cn.com/problems/closest-binary-search-tree-value/description/
#
# algorithms
# Easy (52.70%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 11.3K
# Testcase Example:  '[4,2,5,1,3]\n3.714286'
#
# 给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。
# 
# 注意：
# 
# 
# 给定的目标值 target 是一个浮点数
# 题目保证在该二叉搜索树中只会存在一个最接近目标值的数
# 
# 
# 示例：
# 
# 输入: root = [4,2,5,1,3]，目标值 target = 3.714286
# 
# ⁠   4
# ⁠  / \
# ⁠ 2   5
# ⁠/ \
# 1   3
# 
# 输出: 4
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
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = float("inf")

        def closest(node: TreeNode):
            nonlocal res

            if not node:
                return
            if abs(node.val - target) < abs(target - res):
                res = node.val
            if target > node.val:
                closest(node.right)
            else:
                closest(node.left)

        closest(root)

        return res

# @lc code=end
