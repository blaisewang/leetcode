#
# @lc app=leetcode.cn id=340 lang=python3
#
# [340] 至多包含 K 个不同字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
# algorithms
# Hard (48.63%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    5.2K
# Total Submissions: 10.6K
# Testcase Example:  '"eceba"\n2'
#
# 给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。
# 
# 示例 1:
# 
# 输入: s = "eceba", k = 2
# 输出: 3
# 解释: 则 T 为 "ece"，所以长度为 3。
# 
# 示例 2:
# 
# 输入: s = "aa", k = 1
# 输出: 2
# 解释: 则 T 为 "aa"，所以长度为 2。
# 
# 
#

# @lc code=start
from collections import OrderedDict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or len(s) == 0:
            return 0

        ml = 1
        l, r = 0, 0
        h = OrderedDict()

        while r < len(s):
            c = s[r]
            if c in h:
                del h[c]
            h[c] = r
            r += 1

            if len(h) == k + 1:
                _, di = h.popitem(last=False)
                l = di + 1

            ml = max(ml, r - l)

        return ml

# @lc code=end
