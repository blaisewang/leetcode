#
# @lc app=leetcode.cn id=1274 lang=python3
#
# [1274] 矩形内船只的数目
#
# https://leetcode-cn.com/problems/number-of-ships-in-a-rectangle/description/
#
# algorithms
# Hard (56.39%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    757
# Total Submissions: 1.3K
# Testcase Example:  '[[1,1],[2,2],[3,3],[5,5]]\n[4,4]\n[0,0]'
#
# (此题是 交互式问题 )
# 
# 在用笛卡尔坐标系表示的二维海平面上，有一些船。每一艘船都在一个整数点上，且每一个整数点最多只有 1 艘船。
# 
# 有一个函数 Sea.hasShips(topRight, bottomLeft)
# ，输入参数为右上角和左下角两个点的坐标，当且仅当这两个点所表示的矩形区域（包含边界）内至少有一艘船时，这个函数才返回 true ，否则返回 false
# 。
# 
# 给你矩形的右上角 topRight 和左下角 bottomLeft 的坐标，请你返回此矩形内船只的数目。题目保证矩形内 至多只有 10 艘船。
# 
# 调用函数 hasShips 超过400次 的提交将被判为 错误答案（Wrong Answer）
# 。同时，任何尝试绕过评测系统的行为都将被取消比赛资格。
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：
# ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
# 输出：3
# 解释：在 [0,0] 到 [4,4] 的范围内总共有 3 艘船。
# 
# 
# 
# 
# 提示：
# 
# 
# ships 数组只用于评测系统内部初始化。你无法得知 ships 的信息，所以只能通过调用 hasShips 接口来求解。
# 0 <= bottomLeft[0] <= topRight[0] <= 1000
# 0 <= bottomLeft[1] <= topRight[1] <= 1000
# 
# 
#

# @lc code=start
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
# class Point(object):
#   def __init__(self, x: int, y: int):
#       self.x = x
#       self.y = y


class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        xl, yl, xr, yr = bottomLeft.x, bottomLeft.y, topRight.x, topRight.y
        x, y = (xl + xr) // 2, (yl + yr) // 2

        if xl == xr and yl == yr:
            return 1
        elif xl == xr:
            return self.countShips(sea, Point(x, y), Point(x, yl)) + self.countShips(sea, Point(x, yr), Point(x, y + 1))
        elif yl == yr:
            return self.countShips(sea, Point(x, y), Point(xl, y)) + self.countShips(sea, Point(xr, y), Point(x + 1, y))
        else:
            return self.countShips(sea, Point(x, y), Point(xl, yl)) + self.countShips(sea, Point(x, yr), Point(xl, y + 1)) + self.countShips(sea, Point(xr, y),  Point(x + 1, yl)) + self.countShips(sea, Point(xr, yr), Point(x + 1, y + 1))

# @lc code=end
