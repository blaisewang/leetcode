#
# @lc app=leetcode.cn id=531 lang=python3
#
# [531] 孤独像素 I
#
# https://leetcode-cn.com/problems/lonely-pixel-i/description/
#
# algorithms
# Medium (66.67%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 3.4K
# Testcase Example:  '[["W","W","B"],["W","B","W"],["B","W","W"]]'
#
# 给定一幅黑白像素组成的图像, 计算黑色孤独像素的数量。
# 
# 图像由一个由‘B’和‘W’组成二维字符数组表示, ‘B’和‘W’分别代表黑色像素和白色像素。
# 
# 黑色孤独像素指的是在同一行和同一列不存在其他黑色像素的黑色像素。
# 
# 示例:
# 
# 输入: 
# [['W', 'W', 'B'],
# ⁠['W', 'B', 'W'],
# ⁠['B', 'W', 'W']]
# 
# 输出: 3
# 解析: 全部三个'B'都是黑色孤独像素。
# 
# 
# 
# 
# 注意:
# 
# 
# 输入二维数组行和列的范围是 [1,500]。
# 
# 
# 
# 
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row, col = [Counter(r)["B"] for r in picture], [Counter(c)["B"] for c in zip(*picture)]
        return sum((row[r] == 1 and col[c] == 1 and picture[r][c] == "B") for r in range(len(picture)) for c in range(len(picture[0])))

# @lc code=end
