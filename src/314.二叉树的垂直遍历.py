#
# @lc app=leetcode.cn id=314 lang=python3
#
# [314] 二叉树的垂直遍历
#
# https://leetcode-cn.com/problems/binary-tree-vertical-order-traversal/description/
#
# algorithms
# Medium (55.07%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    1.8K
# Total Submissions: 3.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其结点 垂直方向（从上到下，逐列）遍历的值。
# 
# 如果两个结点在同一行和列，那么顺序则为 从左到右。
# 
# 示例 1：
# 
# 输入: [3,9,20,null,null,15,7]
# 
# ⁠  3
# ⁠ /\
# ⁠/  \
# 9   20
# ⁠   /\
# ⁠  /  \
# ⁠ 15   7 
# 
# 输出:
# 
# [
# ⁠ [9],
# ⁠ [3,15],
# ⁠ [20],
# ⁠ [7]
# ]
# 
# 
# 示例 2:
# 
# 输入: [3,9,8,4,0,1,7]
# 
# ⁠    3
# ⁠   /\
# ⁠  /  \
# ⁠ 9    8
# ⁠ /\   /\
# ⁠/  \ /  \
# 4   0 1   7 
# 
# 输出:
# 
# [
# ⁠ [4],
# ⁠ [9],
# ⁠ [3,0,1],
# ⁠ [8],
# ⁠ [7]
# ]
# 
# 
# 示例 3:
# 
# 输入: [3,9,8,4,0,1,7,null,null,null,2,5]（注意：0 的右侧子节点为 2，1 的左侧子节点为 5）
# 
# ⁠    3
# ⁠   /\
# ⁠  /  \
# ⁠  9   8
# ⁠ /\  /\
# ⁠/  \/  \
# ⁠4  01   7
# ⁠   /\
# ⁠  /  \
# ⁠  5   2
# 
# 输出:
# 
# [
# ⁠ [4],
# ⁠ [9,5],
# ⁠ [3,0,1],
# ⁠ [8,2],
# ⁠ [7]
# ]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append((root, 0))
        r = defaultdict(list)
        while q:
            n, l = q.popleft()
            r[l].append(n.val)
            if n.left:
                q.append((n.left, l - 1))
            if n.right:
                q.append((n.right, l + 1))

        return [r[x] for x in sorted(r.keys())]

# @lc code=end
