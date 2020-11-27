#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#
# https://leetcode-cn.com/problems/shortest-distance-to-a-character/description/
#
# algorithms
# Easy (65.57%)
# Likes:    121
# Dislikes: 0
# Total Accepted:    12.7K
# Total Submissions: 18.9K
# Testcase Example:  '"loveleetcode"\n"e"'
#
# 给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
# 
# 示例 1:
# 
# 
# 输入: S = "loveleetcode", C = 'e'
# 输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
# 
# 
# 说明:
# 
# 
# 字符串 S 的长度范围为 [1, 10000]。
# C 是一个单字符，且保证是字符串 S 里的字符。
# S 和 C 中的所有字母均为小写字母。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        l = 0
        res = [len(S)] * len(S)

        for r in range(0, len(S)):
            if S[r] is C:
                for i in range(l, r + 1):
                    res[i] = min(res[i], r - i)
                l = r
            elif S[l] is C:
                res[r] = min(res[r], r - l)

        return res

# @lc code=end
