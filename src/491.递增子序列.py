#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#
# https://leetcode-cn.com/problems/increasing-subsequences/description/
#
# algorithms
# Medium (48.91%)
# Likes:    108
# Dislikes: 0
# Total Accepted:    9K
# Total Submissions: 18.3K
# Testcase Example:  '[4,6,7,7]'
#
# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
# 
# 示例:
# 
# 
# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
# [4,7,7]]
# 
# 说明:
# 
# 
# 给定数组的长度不会超过15。
# 数组中的整数范围是 [-100,100]。
# 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        r = []
        visit = set()

        def dfs(index: int, a: list):
            if len(a) > 1 and tuple(a) not in visit:
                r.append(a[:])
                visit.add(tuple(a))

            for j in range(index + 1, len(nums)):
                if nums[j] >= a[-1]:
                    a.append(nums[j])
                    dfs(j, a)
                    a.pop()

        for i, n in enumerate(nums):
            dfs(i, [n])

        return r

# @lc code=end
