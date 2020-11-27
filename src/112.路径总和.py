#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# https://leetcode-cn.com/problems/path-sum/description/
#
# algorithms
# Easy (48.25%)
# Likes:    195
# Dislikes: 0
# Total Accepted:    39K
# Total Submissions: 80.9K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \      \
# ⁠       7    2      1
# 
# 
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if not root:
            return False

        stack = [(root.val, root)]

        while stack:

            val, node = stack.pop()
            if node.right:
                stack.append((val + node.right.val, node.right))
            if node.left:
                stack.append((val + node.left.val, node.left))

            if not node.left and not node.right and val == sum:
                return True

        return False

        # if not root:
        #     return False
        #
        # if not root.left and not root.right:
        #     return root.val == sum
        #
        # return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

# @lc code=end
