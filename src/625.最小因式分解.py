#
# @lc app=leetcode.cn id=625 lang=python3
#
# [625] 最小因式分解
#
# https://leetcode-cn.com/problems/minimum-factorization/description/
#
# algorithms
# Medium (33.56%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    1.9K
# Total Submissions: 5.7K
# Testcase Example:  '48'
#
# 给定一个正整数 a，找出最小的正整数 b 使得 b 的所有数位相乘恰好等于 a。
# 
# 如果不存在这样的结果或者结果不是 32 位有符号整数，返回 0。
# 
# 
# 
# 样例 1
# 
# 输入：
# 
# 48 
# 
# 
# 输出：
# 
# 68
# 
# 
# 
# 样例 2
# 
# 输入：
# 
# 15
# 
# 
# 输出：
# 
# 35
# 
# 
# 
#


# @lc code=start
class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a < 2:
            return a

        r, m = 0, 1
        for i in range(9, 1, -1):
            while a % i == 0:
                a /= i
                r = m * i + r
                m *= 10

        return int(r) if a < 2 and r < 2 ** 31 - 1 else 0

# @lc code=end
