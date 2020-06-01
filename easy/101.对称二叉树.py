#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (49.06%)
# Likes:    517
# Dislikes: 0
# Total Accepted:    72.3K
# Total Submissions: 147.2K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 说明:
# 
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
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
    def isSymmetric(self, root: TreeNode) -> bool:

        def check(l: TreeNode, r: TreeNode) -> bool:
            if not l and not r:
                return True
            if type(l) != type(r):
                return False
            if l.val != r.val:
                return False

            return check(l.left, r.right) and check(l.right, r.left)

        return check(root.left, root.right) if root else True

# @lc code=end
