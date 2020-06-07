#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#
# https://leetcode-cn.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (31.98%)
# Likes:    114
# Dislikes: 0
# Total Accepted:    22.1K
# Total Submissions: 66.2K
# Testcase Example:  '5'
#
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c。
# 
# 示例1:
# 
# 
# 输入: 5
# 输出: True
# 解释: 1 * 1 + 2 * 2 = 5
# 
# 
# 
# 
# 示例2:
# 
# 
# 输入: 3
# 输出: False
# 
# 
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(c ** 0.5)
        while i <= j:
            if i * i + j * j == c:
                return True
            elif i * i + j * j > c:
                j -= 1
            else:
                i += 1
        return False

# @lc code=end
