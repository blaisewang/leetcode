#
# @lc app=leetcode.cn id=1682 lang=python3
#
# [1682] Longest Palindromic Subsequence II
#
# https://leetcode-cn.com/problems/longest-palindromic-subsequence-ii/description/
#
# algorithms
# Medium (64.71%)
# Likes:    2
# Dislikes: 0
# Total Accepted:    62
# Total Submissions: 96
# Testcase Example:  '"bbabab"'
#
# 字符串 s 的某个子序列符合下列条件时，称为“好的回文子序列”：
# 
# 
# 它是 s 的子序列。
# 它是回文序列（反转后与原序列相等）。
# 长度为偶数。
# 除中间的两个字符外，其余任意两个连续字符不相等。
# 
# 
# 例如，若 s = "abcabcabb"，则 "abba" 可称为“好的回文子序列”，而 "bcb" （长度不是偶数）和 "bbbb"
# （含有相等的连续字符）不能称为“好的回文子序列”。
# 
# 给定一个字符串 s， 返回 s 的最长“好的回文子序列”的长度。
# 
# 
# 
# 示例 1:
# 
# 输入: s = "bbabab"
# 输出: 4
# 解释: s 的最长“好的回文子序列”是 "baab"。
# 
# 
# 示例 2:
# 
# 输入: s = "dcbccacdb"
# 输出: 4
# 解释: The longest good palindromic subsequence of s is "dccd".
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= s.length <= 250
# s 包含小写英文字母。
# 
# 
#

# @lc code=start
from bisect import bisect_left, bisect_right
from collections import defaultdict
from functools import lru_cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def find(left: int, right: int) -> int:
            r = 0
            f = s[left - 1] if left else ""
            for letter, ind in li.items():
                if letter == f:
                    continue

                bl, br = bisect_left(ind, left), bisect_right(ind, right)
                if bl < br - 1:
                    r = max(r, find(ind[bl] + 1, ind[br - 1] - 1) + 2)

            return r

        li = defaultdict(list)
        for i, x in enumerate(s):
            li[x].append(i)

        return find(0, len(s) - 1)

# @lc code=end
