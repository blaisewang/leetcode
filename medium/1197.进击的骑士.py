#
# @lc app=leetcode.cn id=1197 lang=python3
#
# [1197] 进击的骑士
#
# https://leetcode-cn.com/problems/minimum-knight-moves/description/
#
# algorithms
# Medium (34.03%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 8.5K
# Testcase Example:  '2\n1'
#
# 一个坐标可以从 -infinity 延伸到 +infinity 的 无限大的 棋盘上，你的 骑士 驻扎在坐标为 [0, 0] 的方格里。
# 
# 骑士的走法和中国象棋中的马相似，走 “日” 字：即先向左（或右）走 1 格，再向上（或下）走 2 格；或先向左（或右）走 2 格，再向上（或下）走 1
# 格。
# 
# 每次移动，他都可以按图示八个方向之一前进。
# 
# 
# 
# 现在，骑士需要前去征服坐标为 [x, y] 的部落，请你为他规划路线。
# 
# 最后返回所需的最小移动次数即可。本题确保答案是一定存在的。
# 
# 
# 
# 示例 1：
# 
# 输入：x = 2, y = 1
# 输出：1
# 解释：[0, 0] → [2, 1]
# 
# 
# 示例 2：
# 
# 输入：x = 5, y = 5
# 输出：4
# 解释：[0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
# 
# 
# 
# 
# 提示：
# 
# 
# |x| + |y| <= 300
# 
# 
#

# @lc code=start
import heapq


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        v = set()
        f1 = (abs(x) + abs(y)) / 3
        q = [(f1, 0, f1, 0, 0)]

        while len(q) > 0:
            _, d1, f1, i1, j1 = heapq.heappop(q)
            if (i1, j1) == (x, y):
                return d1

            for i2, j2 in [
                (i1 - 1, j1 - 2), (i1 - 1, j1 + 2), (i1 + 1, j1 - 2), (i1 + 1, j1 + 2),
                (i1 - 2, j1 - 1), (i1 - 2, j1 + 1), (i1 + 2, j1 - 1), (i1 + 2, j1 + 1)]:
                if (i2, j2) in v:
                    continue

                f2 = (abs(i2 - x) + abs(j2 - y)) / 3
                d2 = d1 + 1
                heapq.heappush(q, (f2 + d2, d2, f2, i2, j2))
                v.add((i2, j2))

# @lc code=end
