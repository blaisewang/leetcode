#
# @lc app=leetcode.cn id=296 lang=python3
#
# [296] 最佳的碰头地点
#
# https://leetcode-cn.com/problems/best-meeting-point/description/
#
# algorithms
# Hard (59.21%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 2.6K
# Testcase Example:  '[[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]'
#
# 有一队人（两人或以上）想要在一个地方碰面，他们希望能够最小化他们的总行走距离。
# 
# 给你一个 2D 网格，其中各个格子内的值要么是 0，要么是 1。
# 
# 1 表示某个人的家所处的位置。这里，我们将使用 曼哈顿距离 来计算，其中 distance(p1, p2) = |p2.x - p1.x| + |p2.y
# - p1.y|。
# 
# 示例：
# 
# 输入: 
# 
# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# 
# 输出: 6 
# 
# 解析: 给定的三个人分别住在(0,0)，(0,4) 和 (2,2):
# (0,2) 是一个最佳的碰面点，其总行走距离为 2 + 2 + 2 = 6，最小，因此返回 6。
# 
#

# @lc code=start
from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        def dist_to_median(l: List[int]) -> int:
            l = sorted(l)
            return sum([abs(num - l[len(l) // 2]) for num in l])

        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        x_s, y_s = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x_s.append(i)
                    y_s.append(j)

        return dist_to_median(x_s) + dist_to_median(y_s)

# @lc code=end
