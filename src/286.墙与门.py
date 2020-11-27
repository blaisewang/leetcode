#
# @lc app=leetcode.cn id=286 lang=python3
#
# [286] 墙与门
#
# https://leetcode-cn.com/problems/walls-and-gates/description/
#
# algorithms
# Medium (46.04%)
# Likes:    59
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 12.4K
# Testcase Example:  '[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]'
#
# 你被给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值：
# 
# 
# -1 表示墙或是障碍物
# 0 表示一扇门
# INF 无限表示一个空的房间。然后，我们用 2^31 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647
# 的。
# 
# 
# 你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。
# 
# 示例：
# 
# 给定二维网格：
# 
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
# ⁠ 0  -1 INF INF
# 
# 
# 运行完你的函数后，该网格应该变成：
# 
# ⁠ 3  -1   0   1
# ⁠ 2   2   1  -1
# ⁠ 1  -1   2  -1
# ⁠ 0  -1   3   4
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        inf = 2 ** 31 - 1
        m, n = len(rooms), len(rooms[0])
        d = ((-1, 0), (1, 0), (0, 1), (0, -1))
        queue = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        while queue:
            x, y = queue.pop(0)
            for dx, dy in d:
                if 0 <= x + dx < m and 0 <= y + dy < n and rooms[x + dx][y + dy] == inf:
                    rooms[x + dx][y + dy] = rooms[x][y] + 1
                    queue.append((x + dx, y + dy))

# @lc code=end
