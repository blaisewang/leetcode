#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (69.95%)
# Likes:    471
# Dislikes: 0
# Total Accepted:    61K
# Total Submissions: 86.8K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 
# 返回 s 所有可能的分割方案。
# 
# 示例:
# 
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
#

# @lc code=start
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        r = []

        def backtrack(ts: str, t):
            if not ts:
                r.append(t)
            for i in range(1, len(ts) + 1):
                if ts[:i] == ts[:i][::-1]:
                    backtrack(ts[i:], t + [ts[:i]])
        backtrack(s, [])

        return r

# @lc code=end
