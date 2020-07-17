#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#
# https://leetcode-cn.com/problems/interleaving-string/description/
#
# algorithms
# Hard (40.54%)
# Likes:    216
# Dislikes: 0
# Total Accepted:    16.9K
# Total Submissions: 41K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
# 
# 示例 1:
# 
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出: false
# 
#


# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if len(s1) + l2 != l3:
            return False

        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]

        dp[0][0] = True
        for i in range(1, l1 + 1):
            dp[i][0] = (dp[i - 1][0] and s1[i - 1] == s3[i - 1])
        for i in range(1, l2 + 1):
            dp[0][i] = (dp[0][i - 1] and s2[i - 1] == s3[i - 1])
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])

        return dp[-1][-1]

# @lc code=end
