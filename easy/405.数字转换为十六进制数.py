#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return "0"

        h, r = "0123456789abcdef", ""
        while num and len(r) < 8:
            r = h[num & 0xf] + r
            num >>= 4

        return r

# @lc code=end
