#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#
# https://leetcode-cn.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (32.30%)
# Likes:    259
# Dislikes: 0
# Total Accepted:    22.3K
# Total Submissions: 61.5K
# Testcase Example:  '"aacecaaa"'
#
# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
# 
# 示例 1:
# 
# 输入: "aacecaaa"
# 输出: "aaacecaaa"
# 
# 
# 示例 2:
# 
# 输入: "abcd"
# 输出: "dcbabcd"
# 
#


# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        b, m = 131, 10 ** 9 + 7
        l = r = 0
        mul = 1
        best = -1

        for i in range(len(s)):
            l = (l * b + ord(s[i])) % m
            r = (r + mul * ord(s[i])) % m
            if l == r:
                best = i
            mul = mul * b % m

        a = "" if best == len(s) - 1 else s[best + 1:]
        return a[::-1] + s

# @lc code=end
