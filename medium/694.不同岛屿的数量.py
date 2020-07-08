#
# @lc app=leetcode.cn id=694 lang=python3
#
# [694] 不同岛屿的数量
#
# https://leetcode-cn.com/problems/number-of-distinct-islands/description/
#
# algorithms
# Medium (47.25%)
# Likes:    28
# Dislikes: 0
# Total Accepted:    1.6K
# Total Submissions: 3.4K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# 给定一个非空01二维数组表示的网格，一个岛屿由四连通（上、下、左、右四个方向）的 1 组成，你可以认为网格的四周被海水包围。
# 
# 请你计算这个网格中共有多少个形状不同的岛屿。两个岛屿被认为是相同的，当且仅当一个岛屿可以通过平移变换（不可以旋转、翻转）和另一个岛屿重合。
# 
# 
# 
# 样例 1:
# 
# 11000
# 11000
# 00011
# 00011
# 
# 
# 给定上图，返回结果 1。
# 
# 
# 
# 样例 2:
# 
# 11011
# 10000
# 00001
# 11011
# 
# 给定上图，返回结果 <font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New,
# monospace">3</font>。
# 
# 注意:
# 
# 11
# 1
# 
# 
# 和
# 
# ⁠1
# 11
# 
# 
# 是不同的岛屿，因为我们不考虑旋转、翻转操作。
# 
# 
# 
# 注释 :  二维数组每维的大小都不会超过50。
# 
#

# @lc code=start
from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        w, h = len(grid), len(grid[0])
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def traverse(x: int, y: int) -> tuple:
            grid[x][y] = 0
            r, q = [], [(x, y)]

            while q:
                x, y = q.pop(0)
                r.append((x, y))
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h and grid[nx][ny]:
                        grid[nx][ny] = 0
                        q.append((nx, ny))

            mx, my = min(r, key=lambda k: k[0])[0], min(r, key=lambda k: k[1])[1]
            return tuple(map(lambda k: (k[0] - mx) * h + k[1] - my, sorted(r)))

        return len(set(traverse(x, y) for x in range(w) for y in range(h) if grid[x][y]))

# @lc code=end
