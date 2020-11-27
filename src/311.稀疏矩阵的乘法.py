#
# @lc app=leetcode.cn id=311 lang=python3
#
# [311] 稀疏矩阵的乘法
#
# https://leetcode-cn.com/problems/sparse-matrix-multiplication/description/
#
# algorithms
# Medium (74.28%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    1.3K
# Total Submissions: 1.7K
# Testcase Example:  '[[1,0,0],[-1,0,3]]\n[[7,0,0],[0,0,0],[0,0,1]]'
#
# 给你两个 稀疏矩阵 A 和 B，请你返回 AB 的结果。你可以默认 A 的列数等于 B 的行数。
# 
# 请仔细阅读下面的示例。
# 
# 
# 
# 示例：
# 
# 输入：
# 
# A = [
# ⁠ [ 1, 0, 0],
# ⁠ [-1, 0, 3]
# ]
# 
# B = [
# ⁠ [ 7, 0, 0 ],
# ⁠ [ 0, 0, 0 ],
# ⁠ [ 0, 0, 1 ]
# ]
# 
# 输出：
# 
# ⁠    |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
# ⁠                 | 0 0 1 |
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        def multi(row, col):
            r, i = 0, 0
            for c in col:
                while i < len(row) and row[i][0] < c[0]:
                    i += 1
                if i < len(row) and row[i][0] == c[0]:
                    r += row[i][1] * c[1]

            return r

        if not A or not A[0] or not B or not B[0]:
            return [[]]

        n, m, k = len(A), len(A[0]), len(B[0])
        rs = [[(j, A[i][j]) for j in range(m) if A[i][j] != 0] for i in range(n)]
        cs = [[(i, B[i][j]) for i in range(m) if B[i][j] != 0] for j in range(k)]

        return [[multi(r, c) for c in cs] for r in rs]

# @lc code=end
