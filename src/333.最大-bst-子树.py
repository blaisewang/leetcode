#
# @lc app=leetcode.cn id=333 lang=python3
#
# [333] 最大 BST 子树
#
# https://leetcode-cn.com/problems/largest-bst-subtree/description/
#
# algorithms
# Medium (42.88%)
# Likes:    44
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 5.1K
# Testcase Example:  '[10,5,15,1,8,null,7]'
#
# 给定一个二叉树，找到其中最大的二叉搜索树（BST）子树，其中最大指的是子树节点数最多的。
# 
# 注意:
# 子树必须包含其所有后代。
# 
# 示例:
# 
# 输入: [10,5,15,1,8,null,7]
# 
# ⁠  10 
# ⁠  / \ 
# ⁠ 5  15 
# ⁠/ \   \ 
# 1   8   7
# 
# 输出: 3
# 解释: 高亮部分为最大的 BST 子树。
# ⁠    返回值 3 在这个样例中为子树大小。
# 
# 
# 进阶:
# 你能想出用 O(n) 的时间复杂度解决这个问题吗？
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
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def traverse(n: TreeNode):
            if not n:
                return float("inf"), float("-inf"), 0
            li, la, lv = traverse(n.left)
            ri, ra, rv = traverse(n.right)
            if la < n.val < ri:
                return min(n.val, li), max(n.val, ra), lv + rv + 1
            return float("-inf"), float("inf"), max(lv, rv)

        return traverse(root)[2]

# @lc code=end
