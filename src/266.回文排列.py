#
# @lc app=leetcode.cn id=266 lang=python3
#
# [266] 回文排列
#
# https://leetcode-cn.com/problems/palindrome-permutation/description/
#
# algorithms
# Easy (65.23%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 6.5K
# Testcase Example:  '"code"'
#
# 给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。
# 
# 示例 1：
# 
# 输入: "code"
# 输出: false
# 
# 示例 2：
# 
# 输入: "aab"
# 输出: true
# 
# 示例 3：
# 
# 输入: "carerac"
# 输出: true
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        f = False
        d = Counter(s)
        for v in d.values():
            if v % 2 == 1:
                if f:
                    return False
                f = True

        return True

# @lc code=end
