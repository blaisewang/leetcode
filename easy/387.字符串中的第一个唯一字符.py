#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:

        count = Counter(s)

        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1

# @lc code=end
