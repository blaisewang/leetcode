#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#
# https://leetcode-cn.com/problems/min-cost-to-connect-all-points/description/
#
# algorithms
# Medium (51.66%)
# Likes:    40
# Dislikes: 0
# Total Accepted:    4.4K
# Total Submissions: 8.3K
# Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
#
# 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
# 
# 连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示
# val 的绝对值。
# 
# 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# 输出：20
# 解释：
# 
# 我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
# 注意到任意两个点之间只有唯一一条路径互相到达。
# 
# 
# 示例 2：
# 
# 
# 输入：points = [[3,12],[-2,5],[-4,1]]
# 输出：18
# 
# 
# 示例 3：
# 
# 
# 输入：points = [[0,0],[1,1],[1,0],[-1,1]]
# 输出：4
# 
# 
# 示例 4：
# 
# 
# 输入：points = [[-1000000,-1000000],[1000000,1000000]]
# 输出：4000000
# 
# 
# 示例 5：
# 
# 
# 输入：points = [[0,0]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= points.length <= 1000
# -10^6 <= xi, yi <= 10^6
# 所有点 (xi, yi) 两两不同。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0

        f, r = {}, 0

        def find(x: int) -> int:
            f.setdefault(x, x)
            while f[x] != x:
                f[x] = f[f[x]]
                x = f[x]
            return x

        def union(x: int, y: int):
            f[find(x)] = find(y)

        cl = []
        for i in range(len(points) - 1):
            for j in range(1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                cost = abs(xi - xj) + abs(yi - yj)
                cl.append((cost, i, j))
        cl.sort(key=lambda x: x[0])

        for cost, i, j in cl:
            if find(i) != find(j):
                union(i, j)
                r += cost

        return r

# @lc code=end
