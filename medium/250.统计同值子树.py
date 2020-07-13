#
# @lc app=leetcode.cn id=250 lang=python3
#
# [250] 统计同值子树
#
# https://leetcode-cn.com/problems/count-univalue-subtrees/description/
#
# algorithms
# Medium (63.86%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    2.1K
# Total Submissions: 3.3K
# Testcase Example:  '[5,1,5,5,5,null,5]'
#
# 给定一个二叉树，统计该二叉树数值相同的子树个数。
# 
# 同值子树是指该子树的所有节点都拥有相同的数值。
# 
# 示例：
# 
# 输入: root = [5,1,5,5,5,null,5]
# 
# ⁠             5
# ⁠            / \
# ⁠           1   5
# ⁠          / \   \
# ⁠         5   5   5
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

    def countUnivalSubtrees(self, root):
        count = 0

        def is_valid_part(node, val):
            nonlocal count
            if node is None:
                return True

            if not all([is_valid_part(node.left, node.val),
                        is_valid_part(node.right, node.val)]):
                return False

            count += 1
            return node.val == val

        is_valid_part(root, 0)
        return count

# @lc code=end
