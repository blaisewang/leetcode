#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (70.72%)
# Likes:    485
# Dislikes: 0
# Total Accepted:    68.7K
# Total Submissions: 97.1K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给定一个二叉树，原地将它展开为一个单链表。
# 
# 
# 
# 例如，给定二叉树
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 将其展开为：
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        c = root
        while c:
            if c.left:
                p = n = c.left
                while p.right:
                    p = p.right
                p.right = c.right
                c.left = None
                c.right = n
            c = c.right

# @lc code=end
