#
# @lc app=leetcode.cn id=573 lang=python3
#
# [573] 松鼠模拟
#
# https://leetcode-cn.com/problems/squirrel-simulation/description/
#
# algorithms
# Medium (65.81%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    571
# Total Submissions: 868
# Testcase Example:  '5\n7\n[2,2]\n[4,4]\n[[3,0], [2,5]]'
#
# 
# 现在有一棵树，一只松鼠和一些坚果。位置由二维网格的单元格表示。你的目标是找到松鼠收集所有坚果的最小路程，且坚果是一颗接一颗地被放在树下。松鼠一次最多只能携带一颗坚果，松鼠可以向上，向下，向左和向右四个方向移动到相邻的单元格。移动次数表示路程。
# 
# 输入 1:
# 
# 输入: 
# 高度 : 5
# 宽度 : 7
# 树的位置 : [2,2]
# 松鼠 : [4,4]
# 坚果 : [[3,0], [2,5]]
# 输出: 12
# 解释:
# ​​​​​
# 
# 
# 注意:
# 
# 
# 所有给定的位置不会重叠。
# 松鼠一次最多只能携带一颗坚果。
# 给定的坚果位置没有顺序。
# 高度和宽度是正整数。 3 <= 高度 * 宽度 <= 10,000。
# 给定的网格至少包含一颗坚果，唯一的一棵树和一只松鼠。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def getDistance(a: list, b: list) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        r = int(1e9)
        s = sum(getDistance(nut, tree) for nut in nuts) * 2
        for nut in nuts:
            c = s - getDistance(nut, tree) + getDistance(nut, squirrel)
            r = min(c, r)

        return r

# @lc code=end
