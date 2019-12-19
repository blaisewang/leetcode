#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:

        def ones(s):
            return bin(s).count('1')

        r = []
        for h in range(12):
            for m in range(60):
                times = ones(h) + ones(m)
                if times == num:
                    r.append(str(h) + ":" + str(m).zfill(2))

        return r

# @lc code=end
