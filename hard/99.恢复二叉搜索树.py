#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#
# https://leetcode-cn.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (57.51%)
# Likes:    250
# Dislikes: 0
# Total Accepted:    21.3K
# Total Submissions: 37K
# Testcase Example:  '[1,3,null,null,2]'
#
# 二叉搜索树中的两个节点被错误地交换。
# 
# 请在不改变其结构的情况下，恢复这棵树。
# 
# 示例 1:
# 
# 输入: [1,3,null,null,2]
# 
# 1
# /
# 3
# \
# 2
# 
# 输出: [3,1,null,null,2]
# 
# 3
# /
# 1
# \
# 2
# 
# 
# 示例 2:
# 
# 输入: [3,1,4,null,null,2]
# 
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
# 
# 输出: [2,1,4,null,null,3]
# 
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
# 
# 进阶:
# 
# 
# 使用 O(n) 空间复杂度的解法很容易实现。
# 你能想出一个只使用常数空间的解决方案吗？
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        a = [None, None, None]
        while root:
            t = root.left
            if t:
                while t.right and t.right != root:
                    t = t.right
                if t.right:
                    t.right = None
                else:
                    t.right = root
                    root = root.left
                    continue
            if a[0] and root.val < a[0].val:
                if not a[1]:
                    a[1] = a[0]
                a[2] = root
            a[0] = root
            root = root.right
        a[1].val, a[2].val = a[2].val, a[1].val

# @lc code=end
