#
# @lc app=leetcode.cn id=1102 lang=python3
#
# [1102] 得分最高的路径
#
# https://leetcode-cn.com/problems/path-with-maximum-minimum-value/description/
#
# algorithms
# Medium (33.61%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    3K
# Total Submissions: 9K
# Testcase Example:  '[[5,4,5],[1,2,6],[7,4,6]]'
#
# 给你一个 R 行 C 列的整数矩阵 A。矩阵上的路径从 [0,0] 开始，在 [R-1,C-1] 结束。
# 
# 路径沿四个基本方向（上、下、左、右）展开，从一个已访问单元格移动到任一相邻的未访问单元格。
# 
# 路径的得分是该路径上的 最小 值。例如，路径 8 →  4 →  5 →  9 的值为 4 。
# 
# 找出所有路径中得分 最高 的那条路径，返回其 得分。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[[5,4,5],[1,2,6],[7,4,6]]
# 输出：4
# 解释： 
# 得分最高的路径用黄色突出显示。 
# 
# 
# 示例 2：
# 
# 
# 
# 输入：[[2,2,1,2,2,2],[1,2,2,2,1,2]]
# 输出：2
# 
# 示例 3：
# 
# 
# 
# 输入：[[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
# 输出：3
# 
# 
# 
# 提示：
# 
# 
# 1 <= R, C <= 100
# 0 <= A[i][j] <= 10^9
# 
# 
#

# @lc code=start
from typing import List


class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.s = [1] * n

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.s[x] < self.s[y]:
            x, y = y, x
        self.p[y] = x
        self.s[x] += self.s[y]


class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        R = len(A)
        C = len(A[0])

        s = set()
        s.add((0, 0))
        s.add((R - 1, C - 1))

        points = []
        for i in range(R):
            for j in range(C):
                points.append((A[i][j], i, j))
        points.sort()

        d = DSU(R * C)
        r = min(A[0][0], A[R - 1][C - 1])
        while d.find(0) != d.find(R * C - 1):
            p, x, y = points.pop()
            r = min(r, p)
            for i, j in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                if (i, j) in s:
                    d.union(x * C + y, i * C + j)
                s.add((x, y))

        return r

# @lc code=end
