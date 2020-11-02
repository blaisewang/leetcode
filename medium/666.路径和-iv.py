#
# @lc app=leetcode.cn id=666 lang=python3
#
# [666] 路径和 IV
#
# https://leetcode-cn.com/problems/path-sum-iv/description/
#
# algorithms
# Medium (61.03%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    1.3K
# Total Submissions: 2.1K
# Testcase Example:  '[113,215,221]'
#
# 对于一棵深度小于 5 的树，可以用一组三位十进制整数来表示。
# 
# 对于每个整数：
# 
# 
# 百位上的数字表示这个节点的深度 D，1 <= D <= 4。
# 十位上的数字表示这个节点在当前层所在的位置 P， 1 <= P <= 8。位置编号与一棵满二叉树的位置编号相同。
# 个位上的数字表示这个节点的权值 V，0 <= V <= 9。
# 
# 
# 给定一个包含三位整数的升序数组，表示一棵深度小于 5 的二叉树，请你返回从根到所有叶子结点的路径之和。
# 
# 样例 1:
# 
# 输入: [113, 215, 221]
# 输出: 12
# 解释: 
# 这棵树形状如下:
# ⁠   3
# ⁠  / \
# ⁠ 5   1
# 
# 路径和 = (3 + 5) + (3 + 1) = 12.
# 
# 
# 
# 
# 样例 2:
# 
# 输入: [113, 221]
# 输出: 4
# 解释: 
# 这棵树形状如下: 
# ⁠   3
# ⁠    \
# ⁠     1
# 
# 路径和 = (3 + 1) = 4.
# 
# 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree = [-1] * 16
        for n in nums:
            d = n // 100
            p = (n // 10) % 10
            v = n % 10
            i = (2 ** (d - 1) - 1) + p
            tree[i] = v

        r = 0
        for i in range(15, -1, -1):
            if tree[i] == -1:
                continue
            if 8 <= i <= 15 or (tree[2 * i] == tree[2 * i + 1] == -1):
                while i != 0:
                    r += tree[i]
                    i = i // 2

        return r
