#
# @lc app=leetcode.cn id=1631 lang=python3
#
# [1631] 最小体力消耗路径
#
# https://leetcode-cn.com/problems/path-with-minimum-effort/description/
#
# algorithms
# Medium (34.03%)
# Likes:    38
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 10.1K
# Testcase Example:  '[[1,2,2],[3,8,2],[5,3,5]]'
#
# 你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子
# (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0
# 开始编号）。你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。
# 
# 一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。
# 
# 请你返回从左上角走到右下角的最小 体力消耗值 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
# 输出：2
# 解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
# 这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
# 输出：1
# 解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。
# 
# 
# 示例 3：
# 
# 
# 输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# 输出：0
# 解释：上图所示路径不需要消耗任何体力。
# 
# 
# 
# 
# 提示：
# 
# 
# rows == heights.length
# columns == heights[i].length
# 1 
# 1 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        f = {i: i for i in range(rows * cols)}

        def find(x: int) -> int:
            f.setdefault(x, x)
            while f[x] != x:
                f[x] = f[f[x]]
                x = f[x]
            return x

        def union(x: int, y: int):
            f[find(x)] = find(y)

        cl = []
        for i in range(rows):
            for j in range(cols):
                if 0 <= i + 1 < rows:
                    c = abs(heights[i + 1][j] - heights[i][j])
                    cl.append((c, cols * (i + 1) + j, cols * i + j))
                if 0 <= j + 1 < cols:
                    c = abs(heights[i][j + 1] - heights[i][j])
                    cl.append((c, cols * i + j + 1, cols * i + j))

        cl.sort(key=lambda x: x[0])
        for c, point1, point2 in cl:
            union(point1, point2)
            if find(0) == find(rows * cols - 1):
                return c

        return 0

# @lc code=end
