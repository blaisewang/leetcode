#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (57.81%)
# Likes:    446
# Dislikes: 0
# Total Accepted:    87.1K
# Total Submissions: 150K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 
# 示例:
# 
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 
# 说明:
# 
# 
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        j = 0

        for i, num in enumerate(nums):
            if num:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

# @lc code=end
