#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (31.04%)
# Likes:    231
# Dislikes: 0
# Total Accepted:    34.3K
# Total Submissions: 110.1K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
# 
# 示例:
# 
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# 
# 
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 2:
            return 0

        primes = [1] * n
        primes[0] = primes[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(primes)

# @lc code=end
