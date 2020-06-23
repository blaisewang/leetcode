#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#
# https://leetcode-cn.com/problems/shift-2d-grid/description/
#
# algorithms
# Easy (57.29%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    5.6K
# Total Submissions: 9.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n1'
#
# 给你一个 m 行 n 列的二维网格 grid 和一个整数 k。你需要将 grid 迁移 k 次。
# 
# 每次「迁移」操作将会引发下述活动：
# 
# 
# 位于 grid[i][j] 的元素将会移动到 grid[i][j + 1]。
# 位于 grid[i][n - 1] 的元素将会移动到 grid[i + 1][0]。
# 位于 grid[m - 1][n - 1] 的元素将会移动到 grid[0][0]。
# 
# 
# 请你返回 k 次迁移操作后最终得到的 二维网格。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# 输出：[[9,1,2],[3,4,5],[6,7,8]]
# 
# 
# 示例 2：
# 
# 
# 
# 输入：grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# 输出：[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
# 
# 
# 示例 3：
# 
# 输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
# 输出：[[1,2,3],[4,5,6],[7,8,9]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length <= 50
# 1 <= grid[i].length <= 50
# -1000 <= grid[i][j] <= 1000
# 0 <= k <= 100
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        g = [[0] * len(grid[0]) for _ in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                g[(r + (c + k) // len(grid[0])) % len(grid)][(c + k) % len(grid[0])] = grid[r][c]
        return g

# @lc code=end
