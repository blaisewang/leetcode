#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#
# https://leetcode-cn.com/problems/reorganize-string/description/
#
# algorithms
# Medium (43.24%)
# Likes:    144
# Dislikes: 0
# Total Accepted:    11.8K
# Total Submissions: 27.3K
# Testcase Example:  '"aab"'
#
# 给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
# 
# 若可行，输出任意可行的结果。若不可行，返回空字符串。
# 
# 示例 1:
# 
# 
# 输入: S = "aab"
# 输出: "aba"
# 
# 
# 示例 2:
# 
# 
# 输入: S = "aaab"
# 输出: ""
# 
# 
# 注意:
# 
# 
# S 只包含小写字母并且长度在[1, 500]区间内。
# 
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return S

        l = len(S)
        d = Counter(S)
        m = max(d.items(), key=lambda x: x[1])[1]
        if m > (l + 1) // 2:
            return ""

        r = [""] * l
        ei, oi = 0, 1
        hf = l // 2

        for k, c in d.items():
            while 0 < c <= hf and oi < l:
                r[oi] = k
                c -= 1
                oi += 2
            while c > 0:
                r[ei] = k
                c -= 1
                ei += 2

        return "".join(r)

# @lc code=end
