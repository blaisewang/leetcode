#
# @lc app=leetcode.cn id=803 lang=python3
#
# [803] 打砖块
#
# https://leetcode-cn.com/problems/bricks-falling-when-hit/description/
#
# algorithms
# Hard (27.53%)
# Likes:    80
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 5.1K
# Testcase Example:  '[[1,0,0,0],[1,1,1,0]]\n[[1,0]]'
#
# 有一个 m x n 的二元网格，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：
# 
# 
# 一块砖直接连接到网格的顶部，或者
# 至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
# 
# 
# 给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli)
# 位置上的砖块时，对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而掉落。一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。
# 
# 返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。
# 
# 注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
# 输出：[2]
# 解释：
# 网格开始为：
# [[1,0,0,0]，
# ⁠[1,1,1,0]]
# 消除 (1,0) 处加粗的砖块，得到网格：
# [[1,0,0,0]
# ⁠[0,1,1,0]]
# 两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
# [[1,0,0,0],
# ⁠[0,0,0,0]]
# 因此，结果为 [2] 。
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
# 输出：[0,0]
# 解释：
# 网格开始为：
# [[1,0,0,0],
# ⁠[1,1,0,0]]
# 消除 (1,1) 处加粗的砖块，得到网格：
# [[1,0,0,0],
# ⁠[1,0,0,0]]
# 剩下的砖都很稳定，所以不会掉落。网格保持不变：
# [[1,0,0,0], 
# ⁠[1,0,0,0]]
# 接下来消除 (1,0) 处加粗的砖块，得到网格：
# [[1,0,0,0],
# ⁠[0,0,0,0]]
# 剩下的砖块仍然是稳定的，所以不会有砖块掉落。
# 因此，结果为 [0,0] 。
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 
# grid[i][j] 为 0 或 1
# 1 
# hits[i].length == 2
# 0 i 
# 0 i 
# 所有 (xi, yi) 互不相同
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        for i, j in hits:
            grid[i][j] -= 1

        f = [[0] * n for _ in range(m)]
        q = []
        for j in range(n):
            f[0][j] = 1
            if grid[0][j] == 1:
                q.append((0, j))

        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            i, j = q.pop(0)
            for di, dj in d:
                a, b = i + di, j + dj
                if 0 <= a < m and 0 <= b < n and grid[a][b] == 1 and not f[a][b]:
                    f[a][b] = 1
                    q.append((a, b))

        r = []
        for i, j in hits[::-1]:
            grid[i][j] += 1
            remain = 0
            if grid[i][j] == 1:
                if i != 0:
                    for di, dj in d:
                        a, b = i + di, j + dj
                        if 0 <= a < m and 0 <= b < n and grid[a][b] == 1 and f[a][b]:
                            f[i][j] = 1
                            break
                if f[i][j]:
                    q = [(i, j)]
                    while q:
                        ii, jj = q.pop(0)
                        for di, dj in d:
                            a, b = ii + di, jj + dj
                            if 0 <= a < m and 0 <= b < n and grid[a][b] == 1 and not f[a][b]:
                                f[a][b] = 1
                                remain += 1
                                q.append((a, b))
            r.insert(0, remain)

        return r

# @lc code=end
