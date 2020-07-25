#
# @lc app=leetcode.cn id=469 lang=python3
#
# [469] 凸多边形
#
# https://leetcode-cn.com/problems/convex-polygon/description/
#
# algorithms
# Medium (44.95%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    695
# Total Submissions: 1.6K
# Testcase Example:  '[[0,0],[0,1],[1,1],[1,0]]'
#
# 给定一个按顺序连接的多边形的顶点，判断该多边形是否为凸多边形。（凸多边形的定义）
# 
# 注：
# 
# 
# 顶点个数至少为 3 个且不超过 10,000。
# 坐标范围为 -10,000 到 10,000。
# 你可以假定给定的点形成的多边形均为简单多边形（简单多边形的定义）。换句话说，保证每个顶点处恰好是两条边的汇合点，并且这些边 互不相交 。
# 
# 
# 
# 
# 示例 1：
# 
# [[0,0],[0,1],[1,1],[1,0]]
# 
# 输出： True
# 
# 解释：
# 
# 
# 示例 2：
# 
# [[0,0],[0,10],[10,10],[10,0],[5,5]]
# 
# 输出： False
# 
# 解释：
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        p = 0
        n = len(points)
        for i in range(n):
            x1 = points[(i + 1) % n][0] - points[i][0]
            x2 = points[(i + 2) % n][0] - points[i][0]
            y1 = points[(i + 1) % n][1] - points[i][1]
            y2 = points[(i + 2) % n][1] - points[i][1]
            c = x1 * y2 - x2 * y1
            if c != 0:
                if c * p < 0:
                    return False
                else:
                    p = c
        return True
        
# @lc code=end

