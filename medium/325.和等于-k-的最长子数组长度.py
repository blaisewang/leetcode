#
# @lc app=leetcode.cn id=325 lang=python3
#
# [325] 和等于 k 的最长子数组长度
#
# https://leetcode-cn.com/problems/maximum-size-subarray-sum-equals-k/description/
#
# algorithms
# Medium (49.08%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    3.9K
# Total Submissions: 7.9K
# Testcase Example:  '[1,-1,5,-2,3]\n3'
#
# 给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长子数组长度。如果不存在任意一个符合要求的子数组，则返回 0。
# 
# 注意:
# nums 数组的总和是一定在 32 位有符号整数范围之内的。
# 
# 示例 1:
# 
# 输入: nums = [1, -1, 5, -2, 3], k = 3
# 输出: 4 
# 解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
# 
# 
# 示例 2:
# 
# 输入: nums = [-2, -1, 2, 1], k = 1
# 输出: 2 
# 解释: 子数组 [-1, 2] 和等于 1，且长度最长。
# 
# 进阶:
# 你能使时间复杂度在 O(n) 内完成此题吗?
# 
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        p, r = 0, 0
        d = {0: -1}
        for i, n in enumerate(nums):
            p += n
            if p not in d:
                d[p] = i
            if p - k in d:
                r = max(r, i - d[p - k])

        return r

# @lc code=end
