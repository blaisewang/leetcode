#
# @lc app=leetcode.cn id=1259 lang=python3
#
# [1259] 不相交的握手
#
# https://leetcode-cn.com/problems/handshakes-that-dont-cross/description/
#
# algorithms
# Hard (46.06%)
# Likes:    16
# Dislikes: 0
# Total Accepted:    1.6K
# Total Submissions: 3.5K
# Testcase Example:  '2'
#
# 偶数 个人站成一个圆，总人数为 num_people 。每个人与除自己外的一个人握手，所以总共会有 num_people / 2 次握手。
# 
# 将握手的人之间连线，请你返回连线不会相交的握手方案数。
# 
# 由于结果可能会很大，请你返回答案 模 10^9+7 后的结果。
# 
# 
# 
# 示例 1：
# 
# 输入：num_people = 2
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 
# 输入：num_people = 4
# 输出：2
# 解释：总共有两种方案，第一种方案是 [(1,2),(3,4)] ，第二种方案是 [(2,3),(4,1)] 。
# 
# 
# 示例 3：
# 
# 
# 
# 输入：num_people = 6
# 输出：5
# 
# 
# 示例 4：
# 
# 输入：num_people = 8
# 输出：14
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= num_people <= 1000
# num_people % 2 == 0
# 
# 
#


# @lc code=start
class Solution:
    def numberOfWays(self, num_people: int) -> int:
        memo = {0: 1, 2: 1}
        mod = 10 ** 9 + 7

        def dfs(n: int) -> int:
            if n in memo:
                return memo[n]

            r = 0
            for i in range(1, n, 2):
                r += dfs(i - 1) * dfs(n - i - 1)
            memo[n] = r % mod

            return memo[n]

        return dfs(num_people)

# @lc code=end
