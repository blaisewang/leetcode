#
# @lc app=leetcode.cn id=1230 lang=python3
#
# [1230] 抛掷硬币
#
# https://leetcode-cn.com/problems/toss-strange-coins/description/
#
# algorithms
# Medium (44.68%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    1.6K
# Total Submissions: 3.5K
# Testcase Example:  '[0.4]\n1'
#
# 有一些不规则的硬币。在这些硬币中，prob[i] 表示第 i 枚硬币正面朝上的概率。
# 
# 请对每一枚硬币抛掷 一次，然后返回正面朝上的硬币数等于 target 的概率。
# 
# 
# 
# 示例 1：
# 
# 输入：prob = [0.4], target = 1
# 输出：0.40000
# 
# 
# 示例 2：
# 
# 输入：prob = [0.5,0.5,0.5,0.5,0.5], target = 0
# 输出：0.03125
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= prob.length <= 1000
# 0 <= prob[i] <= 1
# 0 <= target <= prob.length
# 如果答案与标准答案的误差在 10^-5 内，则被视为正确答案。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        if target == 0:
            r = 1
            for p in prob:
                r *= (1 - p)
            return r

        n = len(prob)
        dp = [[0] * (target + 1) for _ in range(n)]
        dp[0][1] = prob[0]
        dp[0][0] = 1 - prob[0]

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] * (1 - prob[i])
        for k in range(1, target + 1):
            for i in range(1, n):
                dp[i][k] = dp[i - 1][k] * (1 - prob[i]) + dp[i - 1][k - 1] * prob[i]

        return dp[n - 1][target]

# @lc code=end
