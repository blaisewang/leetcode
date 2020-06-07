#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#
# https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (62.01%)
# Likes:    121
# Dislikes: 0
# Total Accepted:    20K
# Total Submissions: 30.9K
# Testcase Example:  '[3,9,20,15,7]'
#
# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.
# 
# 示例 1:
# 
# 输入:
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 输出: [3, 14.5, 11]
# 解释:
# 第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
# 
# 
# 注意：
# 
# 
# 节点值的范围在32位有符号整数范围内。
# 
# 
#

# @lc code=start
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        queue = deque([root])

        while queue:
            node_sum = 0
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                node_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(node_sum / n)

        return res

# @lc code=end
