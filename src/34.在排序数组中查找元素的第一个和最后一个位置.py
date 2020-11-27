#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (38.25%)
# Likes:    489
# Dislikes: 0
# Total Accepted:    105.5K
# Total Submissions: 264.8K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 如果数组中不存在目标值，返回 [-1, -1]。
# 
# 示例 1:
# 
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 
# 示例 2:
# 
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
# 
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        if not nums or nums[l] != target:
            return [-1, -1]

        a, b = l, len(nums) - 1
        while a < b:
            mid = (a + b + 1) // 2
            if nums[mid] <= target:
                a = mid
            else:
                b = mid - 1

        return [l, a]

# @lc code=end

