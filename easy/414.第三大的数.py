#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
import math
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        r = [float("-inf"), float("-inf"), float("-inf")]
        for n in nums:
            if n in r:
                continue
            if n > r[0]:
                r = [n, r[0], r[1]]
            elif n > r[1]:
                r = [r[0], n, r[1]]
            elif n > r[2]:
                r[2] = n

        return r[0] if math.isinf(r[2]) else r[2]

# @lc code=end
