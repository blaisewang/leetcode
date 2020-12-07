#
# @lc app=leetcode.cn id=272 lang=python3
#
# [272] 最接近的二叉搜索树值 II
#
# https://leetcode-cn.com/problems/closest-binary-search-tree-value-ii/description/
#
# algorithms
# Hard (63.18%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    2.1K
# Total Submissions: 3.3K
# Testcase Example:  '[4,2,5,1,3]\n3.714286\n2'
#
# 给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的 k 个值。
# 
# 注意：
# 
# 
# 给定的目标值 target 是一个浮点数
# 你可以默认 k 值永远是有效的，即 k ≤ 总结点数
# 题目保证该二叉搜索树中只会存在一种 k 个值集合最接近目标值
# 
# 
# 示例：
# 
# 输入: root = [4,2,5,1,3]，目标值 = 3.714286，且 k = 2
# 
# ⁠   4
# ⁠  / \
# ⁠ 2   5
# ⁠/ \
# 1   3
# 
# 输出: [4,3]
# 
# 拓展：
# 假设该二叉搜索树是平衡的，请问您是否能在小于 O(n)（n 为总结点数）的时间复杂度内解决该问题呢？
# 
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        if not root:
            return []

        r = []

        def traverse(node: TreeNode):
            if not node:
                return
            traverse(node.left)
            if k > len(r):
                r.append(node.val)
            elif abs(r[0] - target) > abs(node.val - target):
                r.pop(0)
                r.append(node.val)
            else:
                return
            traverse(node.right)

        traverse(root)

        return r

# @lc code=end
