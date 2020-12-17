#
# @lc app=leetcode.cn id=656 lang=python3
#
# [656] 金币路径
#
# https://leetcode-cn.com/problems/coin-path/description/
#
# algorithms
# Hard (30.01%)
# Likes:    26
# Dislikes: 0
# Total Accepted:    577
# Total Submissions: 1.9K
# Testcase Example:  '[1,2,4,-1,2]\n2'
#
# 给定一个数组 A（下标从 1 开始）包含 N 个整数：A1，A2，……，AN 和一个整数 B。你可以从数组 A 中的任何一个位置（下标为 i）跳到下标
# i+1，i+2，……，i+B 的任意一个可以跳到的位置上。如果你在下标为 i 的位置上，你需要支付 Ai 个金币。如果 Ai 是 -1，意味着下标为 i
# 的位置是不可以跳到的。
# 
# 现在，你希望花费最少的金币从数组 A 的 1 位置跳到 N 位置，你需要输出花费最少的路径，依次输出所有经过的下标（从 1 到 N）。
# 
# 如果有多种花费最少的方案，输出字典顺序最小的路径。
# 
# 如果无法到达 N 位置，请返回一个空数组。
# 
# 
# 
# 样例 1 :
# 
# 输入: [1,2,4,-1,2], 2
# 输出: [1,3,5]
# 
# 
# 
# 
# 样例 2 :
# 
# 输入: [1,2,4,-1,2], 1
# 输出: []
# 
# 
# 
# 
# 注释 :
# 
# 
# 路径 Pa1，Pa2，……，Pan 是字典序小于 Pb1，Pb2，……，Pbm 的，当且仅当第一个 Pai 和 Pbi 不同的 i 满足 Pai <
# Pbi，如果不存在这样的 i 那么满足 n < m。
# A1 >= 0。 A2, ..., AN （如果存在） 的范围是 [-1, 100]。
# A 数组的长度范围 [1, 1000].
# B 的范围 [1, 100].
# 
# 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def cheapestJump(self, A: List[int], B: int) -> List[int]:
        if A[0] == -1 or A[-1] == -1:
            return []

        N = len(A)
        index = [-1 for _ in range(N)]
        dp = [float("inf") for _ in range(N)]
        dp[-1] = 0

        for i in range(N - 2, -1, -1):
            if A[i] == -1:
                continue
            for j in range(1, B + 1):
                if i + j < N:
                    if dp[i] > dp[i + j]:
                        dp[i] = dp[i + j]
                        index[i] = i + j
            dp[i] += A[i]

        i = 0
        r = [1]
        while i <= N - 1 and index[i] > 0:
            r.append(index[i] + 1)
            i = index[i]
        if i == N - 1 and A[-1] != -1:
            return r

        return []

# @lc code=end
