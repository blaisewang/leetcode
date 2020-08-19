#
# @lc app=leetcode.cn id=546 lang=python3
#
# [546] 移除盒子
#
# https://leetcode-cn.com/problems/remove-boxes/description/
#
# algorithms
# Hard (51.12%)
# Likes:    137
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 7.6K
# Testcase Example:  '[1,3,2,2,2,3,4,3,1]\r'
#
# 给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
# 你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k*k
# 个积分。
# 当你将所有盒子都去掉之后，求你能获得的最大积分和。
# 
# 
# 
# 示例：
# 
# 输入：boxes = [1,3,2,2,2,3,4,3,1]
# 输出：23
# 解释：
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 分) 
# ----> [1, 3, 3, 3, 1] (1*1=1 分) 
# ----> [1, 1] (3*3=9 分) 
# ----> [] (2*2=4 分)
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= boxes.length <= 100
# 1 <= boxes[i] <= 100
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        m = {}

        def dp(l, r, n):
            nonlocal m, boxes
            if m.get((l, r, n)):
                return m[(l, r, n)]

            if l == r - 1:
                return (n + 1) * (n + 1)

            if boxes[l] == boxes[l + 1]:
                return dp(l + 1, r, n + 1)

            res = (n + 1) * (n + 1) + dp(l + 1, r, 0)

            for l2 in range(l + 2, r):
                if boxes[l2] == boxes[l]:
                    res = max(res, dp(l + 1, l2, 0) + dp(l2, r, n + 1))

            m[(l, r, n)] = res

            return res

        return dp(0, len(boxes), 0)

# @lc code=end
