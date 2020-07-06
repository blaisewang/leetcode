#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (24.71%)
# Likes:    2342
# Dislikes: 0
# Total Accepted:    269.9K
# Total Submissions: 949.5K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        r = list()

        for f in range(n):
            if f > 0 and nums[f] == nums[f - 1]:
                continue
            t = n - 1
            tar = -nums[f]
            for s in range(f + 1, n):
                if s > f + 1 and nums[s] == nums[s - 1]:
                    continue
                while s < t and nums[s] + nums[t] > tar:
                    t -= 1
                if s == t:
                    break
                if nums[s] + nums[t] == tar:
                    r.append([nums[f], nums[s], nums[t]])

        return r

# @lc code=end
