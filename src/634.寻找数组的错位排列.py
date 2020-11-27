#
# @lc app=leetcode.cn id=634 lang=python3
#
# [634] 寻找数组的错位排列
#
# https://leetcode-cn.com/problems/find-the-derangement-of-an-array/description/
#
# algorithms
# Medium (42.18%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    915
# Total Submissions: 2.2K
# Testcase Example:  '1'
#
# 在组合数学中，如果一个排列中所有元素都不在原先的位置上，那么这个排列就被称为错位排列。
# 
# 给定一个从 1 到 n 升序排列的数组，你可以计算出总共有多少个不同的错位排列吗？
# 
# 由于答案可能非常大，你只需要将答案对 10^9+7 取余输出即可。
# 
# 
# 
# 样例 1:
# 
# 输入: 3
# 输出: 2
# 解释: 原始的数组为 [1,2,3]。两个错位排列的数组为 [2,3,1] 和 [3,1,2]。
# 
# 
# 
# 
# 注释:
# n 的范围是 [1, 10^6]。
# 
#


# @lc code=start
class Solution:
    def findDerangement(self, n: int) -> int:
        m, s, M = 1, 0, 1000000007
        for i in range(n, -1, -1):
            s = (s + M + m * (1 if i % 2 == 0 else -1)) % M
            m = (m * i) % M

        return int(s)

# @lc code=end
