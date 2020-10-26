#
# @lc app=leetcode.cn id=256 lang=python3
#
# [256] 粉刷房子
#
# https://leetcode-cn.com/problems/paint-house/description/
#
# algorithms
# Medium (57.40%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 10.9K
# Testcase Example:  '[[17,2,17],[16,16,5],[14,3,19]]'
#
# 假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
# 
# 当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的矩阵来表示的。
# 
# 例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1
# 号房子粉刷成绿色的花费，以此类推。请你计算出粉刷完所有房子最少的花费成本。
# 
# 注意：
# 
# 所有花费均为正整数。
# 
# 示例：
# 
# 输入: [[17,2,17],[16,16,5],[14,3,19]]
# 输出: 10
# 解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。
# 最少花费: 2 + 5 + 3 = 10。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        if len(costs) == 0:
            return 0

        p = costs[-1]
        for n in reversed(range(len(costs) - 1)):
            c = costs[n]
            c[0] += min(p[1], p[2])
            c[1] += min(p[0], p[2])
            c[2] += min(p[0], p[1])
            p = c

        return min(p)

# @lc code=end
