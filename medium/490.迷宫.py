#
# @lc app=leetcode.cn id=490 lang=python3
#
# [490] 迷宫
#
# https://leetcode-cn.com/problems/the-maze/description/
#
# algorithms
# Medium (46.62%)
# Likes:    66
# Dislikes: 0
# Total Accepted:    4.1K
# Total Submissions: 8.9K
# Testcase Example:  '[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]\n[0,4]\n[4,4]'
#
# 由空地和墙组成的迷宫中有一个球。球可以向上下左右四个方向滚动，但在遇到墙壁前不会停止滚动。当球停下时，可以选择下一个方向。
# 
# 给定球的起始位置，目的地和迷宫，判断球能否在目的地停下。
# 
# 迷宫由一个0和1的二维数组表示。 1表示墙壁，0表示空地。你可以假定迷宫的边缘都是墙壁。起始位置和目的地的坐标通过行号和列号给出。
# 
# 
# 
# 示例 1:
# 
# 输入 1: 迷宫由以下二维数组表示
# 
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# 
# 输入 2: 起始位置坐标 (rowStart, colStart) = (0, 4)
# 输入 3: 目的地坐标 (rowDest, colDest) = (4, 4)
# 
# 输出: true
# 
# 解析: 一个可能的路径是 : 左 -> 下 -> 左 -> 下 -> 右 -> 下 -> 右。
# 
# 
# 
# 示例 2:
# 
# 输入 1: 迷宫由以下二维数组表示
# 
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# 
# 输入 2: 起始位置坐标 (rowStart, colStart) = (0, 4)
# 输入 3: 目的地坐标 (rowDest, colDest) = (3, 2)
# 
# 输出: false
# 
# 解析: 没有能够使球停在目的地的路径。
# 
# 
# 
# 
# 
# 注意:
# 
# 
# 迷宫中只有一个球和一个目的地。
# 球和目的地都在空地上，且初始时它们不在同一位置。
# 给定的迷宫不包括边界 (如图中的红色矩形), 但你可以假设迷宫的边缘都是墙壁。
# 迷宫至少包括2块空地，行数和列数均不超过100。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        d = {(0, 1), (1, 0), (-1, 0), (0, -1)}

        q = [(start[0], start[1])]
        maze[start[0]][start[1]] = -1

        while q:
            i, j = q.pop(0)
            if i == destination[0] and j == destination[1]:
                return True

            for dx, dy in d:
                x, y = i, j
                while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and (maze[x + dx][y + dy] == 0 or maze[x + dx][y + dy] == -1):
                    x = x + dx
                    y = y + dy
                if maze[x][y] != -1:
                    maze[x][y] = -1
                    q.append((x, y))

        return False

# @lc code=end
