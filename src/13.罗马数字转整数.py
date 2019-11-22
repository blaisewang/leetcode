#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1,
             "V": 5,
             "X": 10,
             "L": 50,
             "C": 100,
             "D": 500,
             "M": 1000}

        ns = [d[r] for r in s]

        return sum(-ns[i] if ns[i] < ns[i + 1] else ns[i] for i in range(len(s) - 1)) + ns[-1]

# @lc code=end
