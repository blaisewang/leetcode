#
# @lc app=leetcode.cn id=1099 lang=python3
#
# [1099] 小于 K 的两数之和
#
# https://leetcode-cn.com/problems/two-sum-less-than-k/description/
#
# algorithms
# Easy (56.98%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 5.6K
# Testcase Example:  '[34,23,1,24,75,33,54,8]\n60'
#
# 给你一个整数数组 nums 和整数 k ，返回最大和 sum ，满足存在 i < j 使得 nums[i] + nums[j] = sum 且 sum <
# k 。如果没有满足此等式的 i,j 存在，则返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [34,23,1,24,75,33,54,8], k = 60
# 输出：58
# 解释：
# 34 和 24 相加得到 58，58 小于 60，满足题意。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [10,20,30], k = 15
# 输出：-1
# 解释：
# 我们无法找到和小于 15 的两个元素。
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        r = -1
        nums.sort()
        lf, rt = 0, len(nums) - 1

        while lf < rt:
            s = nums[lf] + nums[rt]
            if s < k:
                r = max(r, s)
                lf += 1
            else:
                rt -= 1

        return r

# @lc code=end
