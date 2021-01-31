#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#
# https://leetcode-cn.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (28.18%)
# Likes:    201
# Dislikes: 0
# Total Accepted:    18.9K
# Total Submissions: 66.4K
# Testcase Example:  '1\n2'
#
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。
# 
# 如果小数部分为循环小数，则将循环的部分括在括号内。
# 
# 如果存在多个答案，只需返回 任意一个 。
# 
# 对于所有给定的输入，保证 答案字符串的长度小于 10^4 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：numerator = 1, denominator = 2
# 输出："0.5"
# 
# 
# 示例 2：
# 
# 
# 输入：numerator = 2, denominator = 1
# 输出："2"
# 
# 
# 示例 3：
# 
# 
# 输入：numerator = 2, denominator = 3
# 输出："0.(6)"
# 
# 
# 示例 4：
# 
# 
# 输入：numerator = 4, denominator = 333
# 输出："0.(012)"
# 
# 
# 示例 5：
# 
# 
# 输入：numerator = 1, denominator = 5
# 输出："0.2"
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 
# denominator != 0
# 
# 
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        if numerator < 0 or denominator < 0:
            ret = self.fractionToDecimal(abs(numerator), abs(denominator))
            if numerator < 0 and denominator < 0:
                return ret
            else:
                return "-" + ret

        q = numerator % denominator
        ql = [q]
        rl = [numerator // denominator]

        while q:
            rl.append(q * 10 // denominator)
            q = q * 10 % denominator
            if ql and q in ql:
                index = ql.index(q)
                return f"{rl[0]}.{''.join(map(str, rl[1:index + 1]))}({''.join(map(str, rl[index + 1:]))})"
            ql.append(q)

        if len(rl) == 1:
            return str(rl[0])
        return f"{rl[0]}.{''.join(map(str, rl[1:]))}"

# @lc code=end
