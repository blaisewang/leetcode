#
# @lc app=leetcode.cn id=361 lang=python3
#
# [361] 轰炸敌人
#
# https://leetcode-cn.com/problems/bomb-enemy/description/
#
# algorithms
# Medium (53.52%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    1.6K
# Total Submissions: 3K
# Testcase Example:  '[["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]'
#
# 想象一下炸弹人游戏，在你面前有一个二维的网格来表示地图，网格中的格子分别被以下三种符号占据：
# 
# 
# 'W' 表示一堵墙
# 'E' 表示一个敌人
# '0'（数字 0）表示一个空位
# 
# 
# 
# 
# 请你计算一个炸弹最多能炸多少敌人。
# 
# 由于炸弹的威力不足以穿透墙体，炸弹只能炸到同一行和同一列没被墙体挡住的敌人。
# 
# 注意：你只能把炸弹放在一个空的格子里
# 
# 示例:
# 
# 输入: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# 输出: 3 
# 解释: 对于如下网格
# 
# 0 E 0 0 
# E 0 W E 
# 0 E 0 0
# 
# 假如在位置 (1,1) 放置炸弹的话，可以炸到 3 个敌人
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ps = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(x: int, y: int) -> int:
            if x + p[0] < 0 or x + p[0] >= len(grid) or y + p[1] < 0 or y + p[1] >= len(grid[0]) or grid[x + p[0]][y + p[1]] == "W":
                return 0
            if grid[x + p[0]][y + p[1]] == "E":
                return 1 + dfs(x + p[0], y + p[1])
            elif grid[x + p[0]][y + p[1]] == "0":
                return dfs(x + p[0], y + p[1])

        me = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    ce = 0
                    for p in ps:
                        ce += dfs(i, j)
                    me = max(me, ce)

        return me

# @lc code=end
