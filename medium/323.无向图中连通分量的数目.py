#
# @lc app=leetcode.cn id=323 lang=python3
#
# [323] 无向图中连通分量的数目
#
# https://leetcode-cn.com/problems/number-of-connected-components-in-an-undirected-graph/description/
#
# algorithms
# Medium (57.82%)
# Likes:    32
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 6K
# Testcase Example:  '5\n[[0,1],[1,2],[3,4]]'
#
# 给定编号从 0 到 n-1 的 n 个节点和一个无向边列表（每条边都是一对节点），请编写一个函数来计算无向图中连通分量的数目。
# 
# 示例 1:
# 
# 输入: n = 5 和 edges = [[0, 1], [1, 2], [3, 4]]
# 
# ⁠    0          3
# ⁠    |          |
# ⁠    1 --- 2    4 
# 
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: n = 5 和 edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
# 
# ⁠    0           4
# ⁠    |           |
# ⁠    1 --- 2 --- 3
# 
# 输出:  1
# 
# 
# 注意:
# 你可以假设在 edges 中不会出现重复的边。而且由于所以的边都是无向边，[0, 1] 与 [1, 0]  相同，所以它们不会同时在 edges 中出现。
# 
#

# @lc code=start
from collections import Counter
from typing import List


class UF:
    def __init__(self, n):
        self.uf = [-1] * n

    def find(self, idx):
        if self.uf[idx] == -1:
            return idx
        return self.find(self.uf[idx])

    def union(self, i1, i2):
        f1 = self.find(i1)
        f2 = self.find(i2)
        if f1 != f2:
            self.uf[f2] = f1

    def result(self):
        return Counter(self.uf)[-1]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        return uf.result()

# @lc code=end
