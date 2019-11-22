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

        int_sum = 0
        last_r = 1001

        for r in s:
            int_sum += d[r]

            if d[r] > last_r:
                int_sum -= 2 * last_r

            last_r = d[r]

        return int_sum

# @lc code=end
