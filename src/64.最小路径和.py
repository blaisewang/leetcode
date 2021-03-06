#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (65.97%)
# Likes:    587
# Dislikes: 0
# Total Accepted:    123.5K
# Total Submissions: 183.6K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        r, c = len(grid), len(grid[0])
        dp = [[0] * c for _ in range(r)]
        dp[0][0] = grid[0][0]
        for i in range(1, r):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, c):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[r - 1][c - 1]

# @lc code=end
