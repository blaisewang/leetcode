#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(magazine) & Counter(ransomNote) == Counter(ransomNote)

# @lc code=end
