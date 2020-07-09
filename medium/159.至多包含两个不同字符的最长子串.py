#
# @lc app=leetcode.cn id=159 lang=python3
#
# [159] 至多包含两个不同字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/description/
#
# algorithms
# Medium (51.35%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    5.4K
# Total Submissions: 10.6K
# Testcase Example:  '"eceba"'
#
# 给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。
# 
# 示例 1:
# 
# 输入: "eceba"
# 输出: 3
# 解释: t 是 "ece"，长度为3。
# 
# 
# 示例 2:
# 
# 输入: "ccaabbb"
# 输出: 5
# 解释: t 是 "aabbb"，长度为5。
# 
# 
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 3:
            return len(s)

        ml = 2
        l, r = 0, 0
        d = dict()

        while r < len(s):
            if len(d) < 3:
                d[s[r]] = r
                r += 1

            if len(d) == 3:
                di = min(d.values())
                del d[s[min(d.values())]]
                l = di + 1

            ml = max(ml, r - l)

        return ml

# @lc code=end
