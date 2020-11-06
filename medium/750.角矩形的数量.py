#
# @lc app=leetcode.cn id=750 lang=python3
#
# [750] 角矩形的数量
#
# https://leetcode-cn.com/problems/number-of-corner-rectangles/description/
#
# algorithms
# Medium (72.15%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    1.4K
# Total Submissions: 1.9K
# Testcase Example:  '[[0,1,0],[1,0,1],[1,0,1],[0,1,0]]'
#
# 给定一个只包含 0 和 1 的网格，找出其中角矩形的数量。
# 
# 一个「角矩形」是由四个不同的在网格上的 1 形成的轴对称的矩形。注意只有角的位置才需要为 1。并且，4 个 1 需要是不同的。
# 
# 
# 
# 示例 1：
# 
# 输入：grid = 
# [[1, 0, 0, 1, 0],
# ⁠[0, 0, 1, 0, 1],
# ⁠[0, 0, 0, 1, 0],
# ⁠[1, 0, 1, 0, 1]]
# 输出：1
# 解释：只有一个角矩形，角的位置为 grid[1][2], grid[1][4], grid[3][2], grid[3][4]。
# 
# 
# 示例 2：
# 
# 输入：grid = 
# [[1, 1, 1],
# ⁠[1, 1, 1],
# ⁠[1, 1, 1]]
# 输出：9
# 解释：这里有 4 个 2x2 的矩形，4 个 2x3 和 3x2 的矩形和 1 个 3x3 的矩形。
# 
# 
# 示例 3：
# 
# 输入：grid = 
# [[1, 1, 1, 1]]
# 输出：0
# 解释：矩形必须有 4 个不同的角。
# 
# 
# 
# 
# 提示：
# 
# 
# 网格 grid 中行和列的数目范围为 [1, 200]。
# 每个网格 grid[i][j] 中的值不是 0 就是 1 。
# 网格中 1 的个数不会超过 6000。
# 
# 
# 
# 
#

# @lc code=start
from collections import Counter
from itertools import combinations
from typing import List


class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        rows = [[c for c, val in enumerate(row) if val] for row in grid]
        n = sum(len(row) for row in grid)
        sqr = int(n ** .5)

        res = 0
        c = Counter()
        for r, row in enumerate(rows):
            if len(row) >= sqr:
                target = set(row)
                for r2, row2 in enumerate(rows):
                    if r2 <= r and len(row2) >= sqr:
                        continue
                    found = sum(1 for c2 in row2 if c2 in target)
                    res += found * (found - 1) / 2
            else:
                for pair in combinations(row, 2):
                    res += c[pair]
                    c[pair] += 1

        return int(res)
        
# @lc code=end

