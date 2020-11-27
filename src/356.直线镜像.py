#
# @lc app=leetcode.cn id=356 lang=python3
#
# [356] 直线镜像
#
# https://leetcode-cn.com/problems/line-reflection/description/
#
# algorithms
# Medium (29.72%)
# Likes:    9
# Dislikes: 0
# Total Accepted:    769
# Total Submissions: 2.6K
# Testcase Example:  '[[1,1],[-1,1]]'
#
# 在一个二维平面空间中，给你 n 个点的坐标。问，是否能找出一条平行于 y 轴的直线，让这些点关于这条直线成镜像排布？
# 
# 示例 1：
# 
# 输入: [[1,1],[-1,1]]
# 输出: true
# 
# 
# 示例 2：
# 
# 输入: [[1,1],[-1,-1]]
# 输出: false
# 
# 拓展：
# 你能找到比 O(n^2) 更优的解法吗?
# 
#

# @lc code=start
from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if not points:
            return True

        d = {}
        xi, xa = float("inf"), float("-inf")
        for x, y in points:
            xi = min(xi, x)
            xa = max(xa, x)
            d.setdefault(y, []).append(x)
        m = xi + xa

        for v in d.values():
            for x in v:
                if m - x not in v:
                    return False

        return True

# @lc code=end
