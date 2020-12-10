#
# @lc app=leetcode.cn id=317 lang=python3
#
# [317] 离建筑物最近的距离
#
# https://leetcode-cn.com/problems/shortest-distance-from-all-buildings/description/
#
# algorithms
# Hard (47.23%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    2.8K
# Total Submissions: 5.8K
# Testcase Example:  '[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]'
#
# 你是个房地产开发商，想要选择一片空地 建一栋大楼。你想把这栋大楼够造在一个距离周边设施都比较方便的地方，通过调研，你希望从它出发能在 最短的距离和
# 内抵达周边全部的建筑物。请你计算出这个最佳的选址到周边全部建筑物的 最短距离和。
# 
# 
# 
# 提示：
# 
# 你只能通过向上、下、左、右四个方向上移动。
# 
# 给你一个由 0、1 和 2 组成的二维网格，其中：
# 
# 
# 0 代表你可以自由通过和选择建造的空地
# 1 代表你无法通行的建筑物
# 2 代表你无法通行的障碍物
# 
# 
# 
# 
# 示例：
# 
# 输入：[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# 
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# 输出：7 
# 解析：
# 给定三个建筑物 (0,0)、(0,4) 和 (2,2) 以及一个位于 (0,2) 的障碍物。
# 由于总距离之和 3+3+1=7 最优，所以位置 (1,2) 是符合要求的最优地点，故返回7。
# 
# 
# 
# 
# 注意：
# 
# 
# 题目数据保证至少存在一栋建筑物，如果无法按照上述规则返回建房地点，则请你返回 -1。
# 
# 
#

# @lc code=start
from queue import Queue
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if len(grid) != 0 else 0
        if m == 0 or n == 0:
            return -1

        q = Queue()
        v = [[[[0] * n for _ in range(m)] for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.put_nowait((i, j, i, j, 0))
                    v[i][j][i][j] = 1

        sn = q.qsize()
        r = [[[0, 0] for _ in range(n)] for _ in range(m)]

        while not q.empty():
            si, sj, ci, cj, w = q.get_nowait()
            if grid[ci][cj] == 0:
                r[ci][cj][0] += w
                r[ci][cj][1] += 1

            for ii, jj in [(ci - 1, cj), (ci + 1, cj), (ci, cj + 1), (ci, cj - 1)]:
                if 0 <= ii < m and 0 <= jj < n:
                    if grid[ii][jj] == 0 and v[si][sj][ii][jj] == 0:
                        v[si][sj][ii][jj] = 1
                        q.put_nowait((si, sj, ii, jj, w + 1))

        res = 0x7fffffff
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and r[i][j][1] == sn:
                    res = min(res, r[i][j][0])

        return res if res != 0x7fffffff else -1

# @lc code=end
