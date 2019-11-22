#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:

        r = int(str(abs(x))[::-1])

        if x < 0:
            r = -r

        if -2 ** 31 <= r <= 2 ** 31 - 1:
            return r

        return 0

# @lc code=end
