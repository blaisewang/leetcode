#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#
# https://leetcode-cn.com/problems/number-of-boomerangs/description/
#
# algorithms
# Easy (55.79%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    7.9K
# Total Submissions: 14.2K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# 给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k
# 之间的距离相等（需要考虑元组的顺序）。
# 
# 找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。
# 
# 示例:
# 
# 
# 输入:
# [[0,0],[1,0],[2,0]]
# 
# 输出:
# 2
# 
# 解释:
# 两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
# 
# 
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def f(x1, y1):
            d = Counter((x2 - x1) ** 2 + (y2 - y1) ** 2 for x2, y2 in points)
            return sum(t * t - t for t in d.values())

        return sum(f(x1, y1) for x1, y1 in points)

# @lc code=end
