#
# @lc app=leetcode.cn id=360 lang=python3
#
# [360] 有序转化数组
#
# https://leetcode-cn.com/problems/sort-transformed-array/description/
#
# algorithms
# Medium (60.27%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 2.5K
# Testcase Example:  '[-4,-2,2,4]\n1\n3\n5'
#
# 给你一个已经 排好序 的整数数组 nums 和整数 a、b、c。对于数组中的每一个数 x，计算函数值 f(x) = ax^2 + bx +
# c，请将函数值产生的数组返回。
# 
# 要注意，返回的这个数组必须按照 升序排列，并且我们所期望的解法时间复杂度为 O(n)。
# 
# 示例 1：
# 
# 输入: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# 输出: [3,9,15,33]
# 
# 
# 示例 2：
# 
# 输入: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# 输出: [-23,-5,1,7]
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        if not nums:
            return []
        res, s = [], len(nums)

        if a == 0:
            if b == 0:
                return [c for _ in range(s)]
            elif b > 0:
                return [b * x + c for x in nums]
            else:
                return [b * x + c for x in nums[::-1]]

        m = -b / a / 2
        l, r = 0, s - 1
        while l <= r:
            if abs(nums[r] - m) > abs(nums[l] - m):
                x = nums[r]
                r -= 1
            else:
                x = nums[l]
                l += 1
            res.append(a * x * x + b * x + c)

        return res if a < 0 else res[::-1]

# @lc code=end
