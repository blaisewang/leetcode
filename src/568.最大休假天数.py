#
# @lc app=leetcode.cn id=568 lang=python3
#
# [568] 最大休假天数
#
# https://leetcode-cn.com/problems/maximum-vacation-days/description/
#
# algorithms
# Hard (47.78%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    797
# Total Submissions: 1.7K
# Testcase Example:  '[[0,1,1],[1,0,1],[1,1,0]]\n[[1,3,1],[6,0,3],[3,3,3]]'
#
# 力扣想让一个最优秀的员工在 N 个城市间旅行来收集算法问题。
# 但只工作不玩耍，聪明的孩子也会变傻，所以您可以在某些特定的城市和星期休假。您的工作就是安排旅行使得最大化你可以休假的天数，但是您需要遵守一些规则和限制。
# 
# 规则和限制：
# 
# 
# 您只能在 N 个城市之间旅行，用 0 到 N-1 的索引表示。一开始，您在索引为0的城市，并且那天是星期一。
# 这些城市通过航班相连。这些航班用 N*N 矩阵 flights（不一定是对称的）表示，flights[i][j]
# 代表城市i到城市j的航空状态。如果没有城市i到城市j的航班，flights[i][j] = 0；否则，flights[i][j] =
# 1。同时，对于所有的i，flights[i][i] = 0。
# 您总共有 K
# 周（每周7天）的时间旅行。您每天最多只能乘坐一次航班，并且只能在每周的星期一上午乘坐航班。由于飞行时间很短，我们不考虑飞行时间的影响。
# 对于每个城市，不同的星期您休假天数是不同的，给定一个 N*K 矩阵 days 代表这种限制，days[i][j]
# 代表您在第j个星期在城市i能休假的最长天数。
# 
# 
# 给定 flights 矩阵和 days 矩阵，您需要输出 K 周内可以休假的最长天数。
# 
# 示例 1:
# 
# 输入:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]
# 输出: 12
# 解释: 
# Ans = 6 + 3 + 3 = 12. 
# 
# 最好的策略之一：
# 第一个星期 : 星期一从城市0飞到城市1，玩6天，工作1天。 
# （虽然你是从城市0开始，但因为是星期一，我们也可以飞到其他城市。） 
# 第二个星期 : 星期一从城市1飞到城市2，玩3天，工作4天。
# 第三个星期 : 呆在城市2，玩3天，工作4天。
# 
# 
# 
# 
# 示例 2:
# 
# 输入:flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]
# 输出: 3
# 解释: 
# Ans = 1 + 1 + 1 = 3. 
# 
# 由于没有航班可以让您飞到其他城市，你必须在城市0呆整整3个星期。 
# 对于每一个星期，你只有一天时间玩，剩下六天都要工作。 
# 所以最大休假天数为3.
# 
# 
# 
# 
# 示例 3:
# 
# 输入:flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]]
# 输出: 21
# 解释:
# Ans = 7 + 7 + 7 = 21
# 
# 最好的策略之一是：
# 第一个星期 : 呆在城市0，玩7天。 
# 第二个星期 : 星期一从城市0飞到城市1，玩7天。
# 第三个星期 : 星期一从城市1飞到城市2，玩7天。
# 
# 
# 
# 
# 注意:
# 
# 
# N 和 K 都是正整数，在 [1, 100] 范围内。
# 矩阵 flights 的所有值都是 [0, 1] 范围内的整数。
# 矩阵 days 的所有值都是 [0, 7] 范围内的整数。
# 超过休假天数您仍可以呆在那个城市，但是在额外的日子您需要 工作 ，这些日子不会算做休假日。
# 如果您从城市A飞往城市B并在当天休假日，这个休假会被算作是城市B的休假日。
# 我们不考虑飞行时间对计算休假日的影响。
# 
# 
# 
# 
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(city: int, week: int) -> int:
            if week >= len(days[0]):
                return 0
            tmp = dp(city, week + 1)
            for idx in range(len(flights)):
                if flights[city][idx] == 1:
                    tmp = max(tmp, dp(idx, week + 1))
            return days[city][week] + tmp

        r = dp(0, 0)
        for i in range(len(flights)):
            if flights[0][i] == 1:
                r = max(r, dp(i, 0))

        return r

# @lc code=end
