#
# @lc app=leetcode.cn id=660 lang=python3
#
# [660] 移除 9
#
# https://leetcode-cn.com/problems/remove-9/description/
#
# algorithms
# Hard (62.26%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    452
# Total Submissions: 726
# Testcase Example:  '9'
#
# 从 1 开始，移除所有包含数字 9 的所有整数，例如 9，19，29，……
# 
# 这样就获得了一个新的整数数列：1，2，3，4，5，6，7，8，10，11，……
# 
# 给定正整数 n，请你返回新数列中第 n 个数字是多少。1 是新数列中的第一个数字。
# 
# 
# 
# 样例 1:
# 
# 输入: 9
# 输出: 10
# 
# 
# 
# 
# 注释 ：n 不会超过 9 x 10^8。
# 
#


# @lc code=start
class Solution:
    def newInteger(self, n: int) -> int:
        r = ""
        while n:
            r = str(n % 9) + r
            n //= 9

        return int(r)

# @lc code=end
