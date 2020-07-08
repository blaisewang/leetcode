#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
# https://leetcode-cn.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (63.71%)
# Likes:    310
# Dislikes: 0
# Total Accepted:    52.1K
# Total Submissions: 81.7K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。
# 
# 一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被
# 0（代表水）包围着。
# 
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
# 
# 
# 
# 示例 1:
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# 
# 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
# 
# 示例 2:
# 
# [[0,0,0,0,0,0,0,0]]
# 
# 对于上面这个给定的矩阵, 返回 0。
# 
# 
# 
# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。
# 
#

# @lc code=start
from typing import List


class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        w, h = len(grid), len(grid[0])
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def traverse(ix: int, iy: int) -> int:
            grid[ix][iy] = 0
            r, q = [], [(ix, iy)]

            while q:
                x, y = q.pop(0)
                r.append((x, y))
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h and grid[nx][ny]:
                        grid[nx][ny] = 0
                        q.append((nx, ny))

            return len(r)

        return max((traverse(x, y) for x in range(w) for y in range(h) if grid[x][y]), default=0)

# @lc code=end
