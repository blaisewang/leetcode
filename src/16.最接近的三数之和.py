#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (42.23%)
# Likes:    503
# Dislikes: 0
# Total Accepted:    132.5K
# Total Submissions: 289.4K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 
# 
# 示例：
# 
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        r = 10 ** 7

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            s, t = i + 1, n - 1
            while s < t:
                st = nums[i] + nums[s] + nums[t]
                if st == target:
                    return target
                if abs(st - target) < abs(r - target):
                    r = st
                if st < target:
                    s0 = s + 1
                    while s0 < t and nums[s0] == nums[s]:
                        s0 += 1
                    s = s0
                else:
                    t0 = t - 1
                    while s < t0 and nums[t0] == nums[t]:
                        t0 -= 1
                    t = t0

        return r

# @lc code=end
