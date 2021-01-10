#
# @lc app=leetcode.cn id=1118 lang=python3
#
# [1118] 一月有多少天
#
# https://leetcode-cn.com/problems/number-of-days-in-a-month/description/
#
# algorithms
# Easy (63.37%)
# Likes:    7
# Dislikes: 0
# Total Accepted:    1.7K
# Total Submissions: 2.7K
# Testcase Example:  '1992\n7'
#
# 指定年份 Y 和月份 M，请你帮忙计算出该月一共有多少天。
# 
# 
# 
# 示例 1：
# 
# 输入：Y = 1992, M = 7
# 输出：31
# 
# 
# 示例 2：
# 
# 输入：Y = 2000, M = 2
# 输出：29
# 
# 
# 示例 3：
# 
# 输入：Y = 1900, M = 2
# 输出：28
# 
# 
# 
# 
# 提示：
# 
# 
# 1583 <= Y <= 2100
# 1 <= M <= 12
# 
# 
#


# @lc code=start
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        if M != 2:
            return 31 if M in {1, 3, 5, 7, 8, 10, 12} else 30

        if Y % 4 == 0:
            if Y % 100 != 0:
                return 29
            else:
                if Y % 400 == 0:
                    return 29
                else:
                    return 28
        else:
            return 28

# @lc code=end
