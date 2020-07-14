#
# @lc app=leetcode.cn id=267 lang=python3
#
# [267] 回文排列 II
#
# https://leetcode-cn.com/problems/palindrome-permutation-ii/description/
#
# algorithms
# Medium (41.05%)
# Likes:    28
# Dislikes: 0
# Total Accepted:    1.4K
# Total Submissions: 3.5K
# Testcase Example:  '"aabb"'
#
# 给定一个字符串 s ，返回其通过重新排列组合后所有可能的回文字符串，并去除重复的组合。
# 
# 如不能形成任何回文排列时，则返回一个空列表。
# 
# 示例 1：
# 
# 输入: "aabb"
# 输出: ["abba", "baab"]
# 
# 示例 2：
# 
# 输入: "abc"
# 输出: []
# 
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        if len(s) < 2:
            return [s]

        d = Counter(s)
        if sum([1 if d[x] % 2 == 1 else 0 for x in d]) > 1:
            return []
        a = [x for x in d if d[x] % 2 == 1]
        if a:
            d[a[0]] -= 1
        s = "".join([x * int(d[x] / 2) for x in d])
        n = len(s)
        res = []

        def helper(t, s):
            if len(t) == n:
                res.append(t + t[::-1])
                return
            for j in range(len(s)):
                if j > 0 and s[j] == s[j - 1]:
                    continue
                helper(t + s[j], s[:j] + s[j + 1:])

        helper("", s)
        if a:
            return [x[:n] + a[0] + x[n:] for x in res]
        else:
            return res

# @lc code=end
