#
# @lc app=leetcode.cn id=1067 lang=python3
#
# [1067] 范围内的数字计数
#
# https://leetcode-cn.com/problems/digit-count-in-range/description/
#
# algorithms
# Hard (39.31%)
# Likes:    16
# Dislikes: 0
# Total Accepted:    595
# Total Submissions: 1.5K
# Testcase Example:  '1\n1\n13'
#
# 给定一个在 0 到 9 之间的整数 d，和两个正整数 low 和 high 分别作为上下界。返回 d 在 low 和 high
# 之间的整数中出现的次数，包括边界 low 和 high。
# 
# 
# 
# 示例 1：
# 
# 输入：d = 1, low = 1, high = 13
# 输出：6
# 解释： 
# 数字 d=1 在 1,10,11,12,13 中出现 6 次。注意 d=1 在数字 11 中出现两次。
# 
# 
# 示例 2：
# 
# 输入：d = 3, low = 100, high = 250
# 输出：35
# 解释：
# 数字 d=3 在 103,113,123,130,131,...,238,239,243 出现 35 次。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= d <= 9
# 1 <= low <= high <= 2×10^8
# 
# 
#

# @lc code=start
class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        r = 0
        sd, sl, sh = str(d), "000000000" + str(low), str(high)
        for k in range(len(sh)):
            unit = 10 ** k
            mul = 1 + high // (unit * 10) - low // (unit * 10)
            if sl[-k - 1] >= sd:
                mul -= 1
            if sh[-k - 1] <= sd:
                mul -= 1
            r += mul * unit
            if sl[-k - 1] == sd and (d != 0 or low >= unit):
                r += unit - low % unit
            if sh[-k - 1] == sd:
                r += high % unit + 1

        return r

# @lc code=end
