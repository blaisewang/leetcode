#
# @lc app=leetcode.cn id=1272 lang=python3
#
# [1272] 删除区间
#
# https://leetcode-cn.com/problems/remove-interval/description/
#
# algorithms
# Medium (49.48%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    1.2K
# Total Submissions: 2.5K
# Testcase Example:  '[[0,2],[3,4],[5,7]]\n[1,6]'
#
# 给你一个 有序的 不相交区间列表 intervals 和一个要删除的区间 toBeRemoved， intervals 中的每一个区间
# intervals[i] = [a, b] 都表示满足 a <= x < b 的所有实数  x 的集合。
# 
# 我们将 intervals 中任意区间与 toBeRemoved 有交集的部分都删除。
# 
# 返回删除所有交集区间后， intervals 剩余部分的 有序 列表。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
# 输出：[[0,1],[6,7]]
# 
# 
# 示例 2：
# 
# 
# 输入：intervals = [[0,5]], toBeRemoved = [2,3]
# 输出：[[0,2],[3,5]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= intervals.length <= 10^4
# -10^9 <= intervals[i][0] < intervals[i][1] <= 10^9
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        r = []

        tl, tr = toBeRemoved
        for x, y in intervals:
            if tl >= y or tr <= x:
                r.append([x, y])
            else:
                if tl > x:
                    r.append([x, tl])
                if tr < y:
                    r.append([tr, y])

        return r

# @lc code=end
