#
# @lc app=leetcode.cn id=280 lang=python3
#
# [280] 摆动排序
#
# https://leetcode-cn.com/problems/wiggle-sort/description/
#
# algorithms
# Medium (67.90%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    2.8K
# Total Submissions: 4.1K
# Testcase Example:  '[3,5,2,1,6,4]'
#
# 给你一个无序的数组 nums, 将该数字 原地 重排后使得 nums[0] <= nums[1] >= nums[2] <= nums[3]...。
# 
# 示例:
# 
# 输入: nums = [3,5,2,1,6,4]
# 输出: 一个可能的解答是 [3,5,1,6,2,4]
# 
#

# @lc code=start
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums) - 1):
            if (i % 2 == 0) == (nums[i] > nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

# @lc code=end
