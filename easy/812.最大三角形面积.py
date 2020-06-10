#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#
# https://leetcode-cn.com/problems/largest-triangle-area/description/
#
# algorithms
# Easy (58.59%)
# Likes:    54
# Dislikes: 0
# Total Accepted:    6.2K
# Total Submissions: 10.3K
# Testcase Example:  '[[0,0],[0,1],[1,0],[0,2],[2,0]]'
#
# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
# 
# 
# 示例:
# 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# 输出: 2
# 解释: 
# 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
# 
# 
# 
# 
# 注意: 
# 
# 
# 3 <= points.length <= 50.
# 不存在重复的点。
# -50 <= points[i][j] <= 50.
# 结果误差值在 10^-6 以内都认为是正确答案。
# 
# 
#

# @lc code=start
import itertools
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(abs((x0 - x2) * (y1 - y2) - (x1 - x2) * (y0 - y2)) for (x0, y0), (x1, y1), (x2, y2) in itertools.combinations(points, 3)) / 2

# @lc code=end
