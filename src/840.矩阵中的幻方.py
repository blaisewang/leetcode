#
# @lc app=leetcode.cn id=840 lang=python3
#
# [840] 矩阵中的幻方
#
# https://leetcode-cn.com/problems/magic-squares-in-grid/description/
#
# algorithms
# Easy (32.57%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 16.8K
# Testcase Example:  '[[4,3,8,4],[9,5,1,9],[2,7,6,2]]'
#
# 3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。
# 
# 给定一个由整数组成的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。
# 
# 
# 
# 示例：
# 
# 输入: [[4,3,8,4],
# ⁠     [9,5,1,9],
# ⁠     [2,7,6,2]]
# 输出: 1
# 解释: 
# 下面的子矩阵是一个 3 x 3 的幻方：
# 438
# 951
# 276
# 
# 而这一个不是：
# 384
# 519
# 762
# 
# 总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
# 
# 
# 提示:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# 0 <= grid[i][j] <= 15
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def is_magic_square(self, s: List[List[int]]) -> bool:
        if s[1][1] != 5:
            return False

        if sorted(n for r in s for n in r) != list(range(1, 10)):
            return False

        return (s[0][0] + s[0][1] + s[0][2] == s[1][0] + s[1][1] + s[1][2] == s[2][0] + s[2][1] + s[2][2] ==
                s[0][0] + s[1][0] + s[2][0] == s[0][1] + s[1][1] + s[2][1] == s[0][2] + s[1][2] + s[2][2] ==
                s[0][0] + s[1][1] + s[2][2] == s[0][2] + s[1][1] + s[2][0] == 15)

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        c = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if self.is_magic_square([grid[i][j: j + 3], grid[i + 1][j: j + 3], grid[i + 2][j: j + 3]]):
                    c += 1

        return c

# @lc code=end
