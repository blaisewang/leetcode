#
# @lc app=leetcode.cn id=259 lang=python3
#
# [259] 较小的三数之和
#
# https://leetcode-cn.com/problems/3sum-smaller/description/
#
# algorithms
# Medium (55.40%)
# Likes:    30
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 5.8K
# Testcase Example:  '[-2,0,1,3]\n2'
#
# 给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 nums[i] + nums[j] + nums[k] < target
# 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。
# 
# 示例：
# 
# 输入: nums = [-2,0,1,3], target = 2
# 输出: 2 
# 解释: 因为一共有两个三元组满足累加和小于 2:
# [-2,0,1]
# ⁠    [-2,0,3]
# 
# 
# 进阶：是否能在 O(n^2) 的时间复杂度内解决？
# 
#

# @lc code=start
from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0

        res = 0
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target - nums[i]:
                    res += r - l
                    l += 1
                else:
                    r -= 1
        return res

# @lc code=end
