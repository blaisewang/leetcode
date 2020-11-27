#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#
# https://leetcode-cn.com/problems/check-if-it-is-a-straight-line/description/
#
# algorithms
# Easy (48.41%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    7K
# Total Submissions: 13.8K
# Testcase Example:  '[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]'
#
# 在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y]
# 表示横坐标为 x、纵坐标为 y 的点。
# 
# 请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 
# 输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates 中不含重复的点
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        r = []
        for i in range(1, len(coordinates)):
            if coordinates[i][0] - coordinates[i - 1][0] == 0:
                k = float("inf")
            else:
                k = (coordinates[i][1] - coordinates[i - 1][1]) / (coordinates[i][0] - coordinates[i - 1][0])
            r.append(k)
        return len(set(r)) == 1

# @lc code=end

