#
# @lc app=leetcode.cn id=302 lang=python3
#
# [302] 包含全部黑色像素的最小矩形
#
# https://leetcode-cn.com/problems/smallest-rectangle-enclosing-black-pixels/description/
#
# algorithms
# Hard (68.27%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    1.2K
# Total Submissions: 1.8K
# Testcase Example:  '[["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]]\n0\n2'
#
# 图片在计算机处理中往往是使用二维矩阵来表示的。
# 
# 假设，这里我们用的是一张黑白的图片，那么 0 代表白色像素，1 代表黑色像素。
# 
# 其中黑色的像素他们相互连接，也就是说，图片中只会有一片连在一块儿的黑色像素（像素点是水平或竖直方向连接的）。
# 
# 那么，给出某一个黑色像素点 (x, y) 的位置，你是否可以找出包含全部黑色像素的最小矩形（与坐标轴对齐）的面积呢？
# 
# 
# 
# 示例:
# 
# 输入:
# [
# ⁠ "0010",
# ⁠ "0110",
# ⁠ "0100"
# ]
# 和 x = 0, y = 2
# 
# 输出: 6
# 
# 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image:
            return 0

        ri, rj = [], []
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == "1":
                    ri.append(i)
                    rj.append(j)

        return ((max(ri) - min(ri)) + 1) * ((max(rj) - min(rj)) + 1)

# @lc code=end
