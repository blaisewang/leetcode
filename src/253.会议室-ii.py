#
# @lc app=leetcode.cn id=253 lang=python3
#
# [253] 会议室 II
#
# https://leetcode-cn.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (44.71%)
# Likes:    115
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 25.3K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# 给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si <
# ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。
# 
# 示例 1:
# 
# 输入: [[0, 30],[5, 10],[15, 20]]
# 输出: 2
# 
# 示例 2:
# 
# 输入: [[7,10],[2,4]]
# 输出: 1
# 
#

# @lc code=start
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        u = 0
        ps, pe = 0, 0
        l = len(intervals)
        s, e = sorted([i[0] for i in intervals]), sorted(i[1] for i in intervals)

        while ps < l:
            if s[ps] >= e[pe]:
                u -= 1
                pe += 1
            u += 1
            ps += 1

        return u

# @lc code=end
