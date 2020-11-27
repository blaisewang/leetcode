#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#
# https://leetcode-cn.com/problems/range-sum-of-bst/description/
#
# algorithms
# Easy (75.57%)
# Likes:    108
# Dislikes: 0
# Total Accepted:    25.3K
# Total Submissions: 33.1K
# Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
#
# 给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
# 
# 二叉搜索树保证具有唯一的值。
# 
# 
# 
# 示例 1：
# 
# 输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
# 输出：32
# 
# 
# 示例 2：
# 
# 输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# 输出：23
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的结点数量最多为 10000 个。
# 最终的答案保证小于 2^31。
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
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        r = 0

        def traverse(node):
            nonlocal r
            if node:
                if L <= node.val <= R:
                    r += node.val
                if L < node.val:
                    traverse(node.left)
                if node.val < R:
                    traverse(node.right)

        traverse(root)
        return r

# @lc code=end
