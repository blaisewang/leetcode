#
# @lc app=leetcode.cn id=644 lang=python3
#
# [644] 最大平均子段和 II
#
# https://leetcode-cn.com/problems/maximum-average-subarray-ii/description/
#
# algorithms
# Hard (36.15%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    677
# Total Submissions: 1.9K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 给定一个包含 n 个整数的数组，找到最大平均值的连续子序列，且长度大于等于 k。并输出这个最大平均值。
# 
# 样例 1:
# 
# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释:
# 当长度为 5 的时候，最大平均值是 10.8，
# 当长度为 6 的时候，最大平均值是 9.16667。
# 所以返回值是 12.75。
# 
# 
# 
# 
# 注释 :
# 
# 
# 1 <= k <= n <= 10,000。
# 数组中的元素范围是 [-10,000, 10,000]。
# 答案的计算误差小于 10^-5 。
# 
# 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def check(avg: int) -> bool:
            end_sum = sum(num - avg for num in nums[:k])
            start_sum = min_start_sum = 0
            for end in range(k, len(nums)):
                if end_sum >= min_start_sum:
                    return True
                end_sum += nums[end] - avg
                start_sum += nums[end - k] - avg
                min_start_sum = min(min_start_sum, start_sum)
            return end_sum >= min_start_sum

        l, r = min(nums), max(nums)
        while r - l > 1e-5:
            mid = (l + r) / 2
            if check(mid):
                l = mid
            else:
                r = mid

        return l

# @lc code=end
