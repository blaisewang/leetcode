#
# @lc app=leetcode.cn id=351 lang=python3
#
# [351] 安卓系统手势解锁
#
# https://leetcode-cn.com/problems/android-unlock-patterns/description/
#
# algorithms
# Medium (57.64%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 5K
# Testcase Example:  '1\n1'
#
# 我们都知道安卓有个手势解锁的界面，是一个 3 x 3 的点所绘制出来的网格。
# 
# 给你两个整数，分别为 ​​m 和 n，其中 1 ≤ m ≤ n ≤ 9，那么请你统计一下有多少种解锁手势，是至少需要经过 m 个点，但是最多经过不超过 n
# 个点的。
# 
# 
# 
# 先来了解下什么是一个有效的安卓解锁手势:
# 
# 
# 每一个解锁手势必须至少经过 m 个点、最多经过 n 个点。
# 解锁手势里不能设置经过重复的点。
# 假如手势中有两个点是顺序经过的，那么这两个点的手势轨迹之间是绝对不能跨过任何未被经过的点。
# 经过点的顺序不同则表示为不同的解锁手势。
# 
# 
# 
# 
# 
# 
# 
# 
# 解释:
# 
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# 
# 无效手势：4 - 1 - 3 - 6 
# 连接点 1 和点 3 时经过了未被连接过的 2 号点。
# 
# 无效手势：4 - 1 - 9 - 2
# 连接点 1 和点 9 时经过了未被连接过的 5 号点。
# 
# 有效手势：2 - 4 - 1 - 3 - 6
# 连接点 1 和点 3 是有效的，因为虽然它经过了点 2 ，但是点 2 在该手势中之前已经被连过了。
# 
# 有效手势：6 - 5 - 4 - 1 - 9 - 2
# 连接点 1 和点 9 是有效的，因为虽然它经过了按键 5 ，但是点 5 在该手势中之前已经被连过了。
# 
# 
# 
# 示例:
# 
# 输入: m = 1，n = 1
# 输出: 9
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        limit = {
            0: [],
            1: [3, 7, 9],
            2: [8],
            3: [1, 7, 9],
            4: [6],
            5: [],
            6: [4],
            7: [1, 3, 9],
            8: [2],
            9: [1, 3, 7]
        }

        def dfs(i: int, u: List[bool], c: int, r: int) -> int:
            if c > n:
                return r

            if m <= c <= n:
                r += 1

            for j in range(1, 10):
                if not u[j] and (j not in limit[i] or u[(i + j) // 2]):
                    u[j] = True
                    c += 1
                    r = dfs(j, u, c, r)
                    u[j] = False
                    c -= 1

            return r

        return dfs(0, [False] * 10, 0, 0)

# @lc code=end
