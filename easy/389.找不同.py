#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return next(iter((Counter(t) - Counter(s))))

# @lc code=end
