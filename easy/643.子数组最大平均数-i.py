#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
# https://leetcode-cn.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (36.51%)
# Likes:    91
# Dislikes: 0
# Total Accepted:    14.9K
# Total Submissions: 38.6K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
# 
# 示例 1:
# 
# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
# 
# 
# 
# 
# 注意:
# 
# 
# 1 <= k <= n <= 30,000。
# 所给数据范围 [-10,000，10,000]。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return sorted(nums)[-1]

        n = 0
        for i in range(k):
            n += nums[i]
        m = n

        for j in range(1, len(nums) - k + 1):
            n = n - nums[j - 1] + nums[j + k - 1]
            m = max(n, m)

        return float(m) / k

# @lc code=end
