#
# @lc app=leetcode.cn id=163 lang=python3
#
# [163] 缺失的区间
#
# https://leetcode-cn.com/problems/missing-ranges/description/
#
# algorithms
# Medium (25.97%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 14.8K
# Testcase Example:  '[0,1,3,50,75]\n0\n99'
#
# 给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。
# 
# 示例：
# 
# 输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
# 输出: ["2", "4->49", "51->74", "76->99"]
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        r = []
        nums = [lower - 1] + nums + [upper + 1]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 2:
                r.append(str(nums[i - 1] + 1) + "->" + str(nums[i] - 1))
            elif nums[i] - nums[i - 1] == 2:
                r.append(str(nums[i] - 1))
        return r

# @lc code=end
