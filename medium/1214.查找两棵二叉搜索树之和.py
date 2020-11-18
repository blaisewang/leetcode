#
# @lc app=leetcode.cn id=1214 lang=python3
#
# [1214] 查找两棵二叉搜索树之和
#
# https://leetcode-cn.com/problems/two-sum-bsts/description/
#
# algorithms
# Medium (60.90%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 3.8K
# Testcase Example:  '[2,1,4]\n[1,0,3]\n5'
#
# 给出两棵二叉搜索树，请你从两棵树中各找出一个节点，使得这两个节点的值之和等于目标值 Target。
# 
# 如果可以找到返回 True，否则返回 False。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：root1 = [2,1,4], root2 = [1,0,3], target = 5
# 输出：true
# 解释：2 加 3 和为 5 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# 每棵树上最多有 5000 个节点。
# -10^9 <= target, node.val <= 10^9
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
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def bst(root: TreeNode, t: int):
            if not root:
                return False
            if root.val == t:
                return True
            if root.val < t:
                return bst(root.right, t)
            if root.val > t:
                return bst(root.left, t)

        def traverse(nl: TreeNode, nr: TreeNode):
            if not nl:
                return False
            if bst(nr, target - nl.val):
                return True
            return traverse(nl.left, nr) or traverse(nl.right, nr)

        return traverse(root1, root2)

# @lc code=end
