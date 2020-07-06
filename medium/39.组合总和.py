#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (67.52%)
# Likes:    750
# Dislikes: 0
# Total Accepted:    107.2K
# Total Submissions: 155K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的数字可以无限制重复被选取。
# 
# 说明：
# 
# 
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        r, p = [], []
        candidates.sort()

        def traverse(begin, size, t):
            if t == 0:
                r.append(p[:])
                return

            for b in range(begin, size):
                residue = t - candidates[b]
                if residue < 0:
                    break
                p.append(candidates[b])
                traverse(b, size, residue)
                p.pop()

        traverse(0, len(candidates), target)
        return r

# @lc code=end
