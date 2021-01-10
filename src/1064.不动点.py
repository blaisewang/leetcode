#
# @lc app=leetcode.cn id=1064 lang=python3
#
# [1064] 不动点
#
# https://leetcode-cn.com/problems/fixed-point/description/
#
# algorithms
# Easy (65.69%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    3.9K
# Total Submissions: 6K
# Testcase Example:  '[-10,-5,0,3,7]'
#
# 给定已经按升序排列、由不同整数组成的数组 A，返回满足 A[i] == i 的最小索引 i。如果不存在这样的 i，返回 -1。
# 
# 
# 
# 示例 1：
# 
# 输入：[-10,-5,0,3,7]
# 输出：3
# 解释：
# 对于给定的数组，A[0] = -10，A[1] = -5，A[2] = 0，A[3] = 3，因此输出为 3 。
# 
# 
# 示例 2：
# 
# 输入：[0,2,5,8,17]
# 输出：0
# 示例：
# A[0] = 0，因此输出为 0 。
# 
# 
# 示例 3：
# 
# 输入：[-10,-5,3,4,7,9]
# 输出：-1
# 解释： 
# 不存在这样的 i 满足 A[i] = i，因此输出为 -1 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length < 10^4
# -10^9 <= A[i] <= 10^9
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        r = 10 ** 9 + 1
        lf, rt = 0, len(A) - 1
        while lf <= rt:
            m = (lf + rt) // 2
            if A[m] == m:
                r = min(r, m)
            if A[m] >= m:
                rt = m - 1
            else:
                lf = m + 1

        return r if r != 10 ** 9 + 1 else -1

# @lc code=end
