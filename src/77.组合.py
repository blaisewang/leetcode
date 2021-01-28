#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (76.11%)
# Likes:    474
# Dislikes: 0
# Total Accepted:    129K
# Total Submissions: 169K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        r, t = [], []

        def backtrack(start):
            if len(t) == k:
                r.append(t[:])

            for i in range(start, n + 1):
                t.append(i)
                backtrack(i + 1)
                t.pop()

        backtrack(1)
        return r

# @lc code=end
