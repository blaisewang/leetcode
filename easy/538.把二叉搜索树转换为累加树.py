#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#
# https://leetcode-cn.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (57.52%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    19.4K
# Total Submissions: 32.5K
# Testcase Example:  '[5,2,13]'
#
# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater
# Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
# 
# 
# 
# 例如：
# 
# 输入: 原始二叉搜索树:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
# 
# 输出: 转换为累加树:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
# 
# 
# 
# 
# 注意：本题和 1038:
# https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同
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
    def __init__(self):
        self.total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)

        return root

# @lc code=end
