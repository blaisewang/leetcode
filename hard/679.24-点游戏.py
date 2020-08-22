#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#
# https://leetcode-cn.com/problems/24-game/description/
#
# algorithms
# Hard (44.57%)
# Likes:    212
# Dislikes: 0
# Total Accepted:    17.1K
# Total Submissions: 31.4K
# Testcase Example:  '[4,1,8,7]'
#
# 你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。
# 
# 示例 1:
# 
# 输入: [4, 1, 8, 7]
# 输出: True
# 解释: (8-4) * (7-1) = 24
# 
# 
# 示例 2:
# 
# 输入: [1, 2, 1, 2]
# 输出: False
# 
# 
# 注意:
# 
# 
# 除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
# 每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1
# 是不允许的。
# 你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        t = 24
        e = 1e-6
        a, m, s, d = 0, 1, 2, 3

        def solve(ns: List[float]) -> bool:
            if not ns:
                return False

            if len(ns) == 1:
                return abs(ns[0] - t) < e

            for i, x in enumerate(ns):
                for j, y in enumerate(ns):
                    if i != j:
                        nn = list()
                        for k, z in enumerate(ns):
                            if k != i and k != j:
                                nn.append(z)
                        for k in range(4):
                            if k < 2 and i > j:
                                continue
                            if k == a:
                                nn.append(x + y)
                            elif k == m:
                                nn.append(x * y)
                            elif k == s:
                                nn.append(x - y)
                            elif k == d:
                                if abs(y) < e:
                                    continue
                                nn.append(x / y)
                            if solve(nn):
                                return True
                            nn.pop()

            return False

        return solve(nums)

# @lc code=end
