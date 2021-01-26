#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (62.36%)
# Likes:    567
# Dislikes: 0
# Total Accepted:    133.6K
# Total Submissions: 213.4K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = []
        check = [0] * len(nums)

        def backtrack(sol):
            if len(sol) == len(nums):
                r.append(sol)
                return

            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    continue
                check[i] = 1
                backtrack(sol + [nums[i]])
                check[i] = 0

        backtrack([])
        return r

# @lc code=end
