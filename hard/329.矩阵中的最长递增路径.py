#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
# https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (41.17%)
# Likes:    219
# Dislikes: 0
# Total Accepted:    16.9K
# Total Submissions: 40.6K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# 给定一个整数矩阵，找出最长递增路径的长度。
# 
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
# 
# 示例 1:
# 
# 输入: nums = 
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ] 
# 输出: 4 
# 解释: 最长递增路径为 [1, 2, 6, 9]。
# 
# 示例 2:
# 
# 输入: nums = 
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ] 
# 输出: 4 
# 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
# 
# 
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix:
            return 0

        rs, cs = len(matrix), len(matrix[0])
        d = {(-1, 0), (1, 0), (0, -1), (0, 1)}

        @lru_cache(None)
        def dfs(row: int, column: int) -> int:
            b = 1
            for dx, dy in d:
                c, r = row + dx, column + dy
                if 0 <= c < rs and 0 <= r < cs and matrix[c][r] > matrix[row][column]:
                    b = max(b, dfs(c, r) + 1)
            return b

        res = 0
        for i in range(rs):
            for j in range(cs):
                res = max(res, dfs(i, j))

        return res

# @lc code=end
