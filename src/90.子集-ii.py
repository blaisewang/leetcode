#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (61.55%)
# Likes:    373
# Dislikes: 0
# Total Accepted:    64K
# Total Submissions: 103.7K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#

# @lc code=start
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()

        def helper(idx: int, t: List[int]):
            r.append(t)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                helper(i + 1, t + [nums[i]])

        helper(0, [])
        return r

# @lc code=end
