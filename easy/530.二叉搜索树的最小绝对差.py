#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (54.80%)
# Likes:    84
# Dislikes: 0
# Total Accepted:    8.6K
# Total Submissions: 15.6K
# Testcase Example:  '[1,null,3,2]'
#
# 给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。
# 
# 示例 :
# 
# 
# 输入:
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
# 
# 输出:
# 1
# 
# 解释:
# 最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
# 
# 
# 注意: 树中至少有2个节点。
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
    def getMinimumDifference(self, root: TreeNode) -> int:
        def pre_order(root):
            if not root:
                return []
            else:
                return pre_order(root.left) + [root.val] + pre_order(root.right)

        target = pre_order(root)
        n = len(target)
        min_ = 10000
        for i in range(n - 1):
            min_ = min(target[i + 1] - target[i], min_)

        return min_

# @lc code=end
