#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#
# https://leetcode-cn.com/problems/base-7/description/
#
# algorithms
# Easy (47.30%)
# Likes:    29
# Dislikes: 0
# Total Accepted:    7.6K
# Total Submissions: 15.9K
# Testcase Example:  '100'
#
# 给定一个整数，将其转化为7进制，并以字符串形式输出。
# 
# 示例 1:
# 
# 
# 输入: 100
# 输出: "202"
# 
# 
# 示例 2:
# 
# 
# 输入: -7
# 输出: "-10"
# 
# 
# 注意: 输入范围是 [-1e7, 1e7] 。
# 
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:

        s, i = 0, 0

        if num < 0:
            h = "-"
            num = abs(num)
        else:
            h = ""

        while num != 0:
            s += ((num % 7) * (10 ** i))
            num //= 7
            i += 1
        return h + str(s)

# @lc code=end
