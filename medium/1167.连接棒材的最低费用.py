#
# @lc app=leetcode.cn id=1167 lang=python3
#
# [1167] 连接棒材的最低费用
#
# https://leetcode-cn.com/problems/minimum-cost-to-connect-sticks/description/
#
# algorithms
# Medium (37.29%)
# Likes:    27
# Dislikes: 0
# Total Accepted:    1.6K
# Total Submissions: 4.2K
# Testcase Example:  '[2,4,3]'
#
# 为了装修新房，你需要加工一些长度为正整数的棒材 sticks。
# 
# 如果要将长度分别为 X 和 Y 的两根棒材连接在一起，你需要支付 X + Y 的费用。 由于施工需要，你必须将所有棒材连接成一根。
# 
# 返回你把所有棒材 sticks 连成一根所需要的最低费用。注意你可以任意选择棒材连接的顺序。
# 
# 
# 
# 示例 1：
# 
# 输入：sticks = [2,4,3]
# 输出：14
# 解释：先将 2 和 3 连接成 5，花费 5；再将 5 和 4 连接成 9；总花费为 14。
# 
# 
# 示例 2：
# 
# 输入：sticks = [1,8,3,5]
# 输出：30
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= sticks.length <= 10^4
# 1 <= sticks[i] <= 10^4
# 
# 
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0

        q = sticks[:]
        heapq.heapify(q)

        r = 0
        while len(q) != 1:
            a = heapq.heappop(q)
            b = heapq.heappop(q)
            r += a + b
            heapq.heappush(q, a + b)

        return r

# @lc code=end
