#
# @lc app=leetcode.cn id=562 lang=python3
#
# [562] 矩阵中最长的连续1线段
#
# https://leetcode-cn.com/problems/longest-line-of-consecutive-one-in-matrix/description/
#
# algorithms
# Medium (43.71%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 5.8K
# Testcase Example:  '[[0,1,1,0],[0,1,1,0],[0,0,0,1]]'
#
# 给定一个01矩阵 M，找到矩阵中最长的连续1线段。这条线段可以是水平的、垂直的、对角线的或者反对角线的。
# 
# 示例:
# 
# 输入:
# [[0,1,1,0],
# ⁠[0,1,1,0],
# ⁠[0,0,0,1]]
# 输出: 3
# 
# 
# 提示: 给定矩阵中的元素数量不会超过 10,000。
# 
#

# @lc code=start
from typing import List

import numpy as np


class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M:
            return 0

        V = np.zeros((len(M) + 2, len(M[0]) + 2))
        H = np.zeros((len(M) + 2, len(M[0]) + 2))
        D = np.zeros((len(M) + 2, len(M[0]) + 2))
        A = np.zeros((len(M) + 2, len(M[0]) + 2))

        for i in range(1, len(V) - 1):
            for j in range(1, len(V[0]) - 1):
                if M[i - 1][j - 1] == 1:
                    V[i][j] = V[i - 1][j] + 1
                    H[i][j] = H[i][j - 1] + 1
                    D[i][j] = D[i - 1][j - 1] + 1
                    A[i][j] = A[i - 1][j + 1] + 1

        r = max(max(max(np.max(V), np.max(H)), np.max(D)), np.max(A))
        return int(r)

# @lc code=end
