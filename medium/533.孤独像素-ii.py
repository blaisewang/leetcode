#
# @lc app=leetcode.cn id=533 lang=python3
#
# [533] 孤独像素 II
#
# https://leetcode-cn.com/problems/lonely-pixel-ii/description/
#
# algorithms
# Medium (50.21%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    980
# Total Submissions: 1.9K
# Testcase Example:  '[["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]]\n' + '3'
#
# 给定一幅由黑色像素和白色像素组成的图像， 与一个正整数N, 找到位于某行 R 和某列 C 中且符合下列规则的黑色像素的数量:
# 
# 
# 行R 和列C都恰好包括N个黑色像素。
# 列C中所有黑色像素所在的行必须和行R完全相同。
# 
# 
# 图像由一个由‘B’和‘W’组成二维字符数组表示, ‘B’和‘W’分别代表黑色像素和白色像素。
# 
# 示例:
# 
# 输入:                                            
# [['W', 'B', 'W', 'B', 'B', 'W'],    
# ⁠['W', 'B', 'W', 'B', 'B', 'W'],    
# ⁠['W', 'B', 'W', 'B', 'B', 'W'],    
# ⁠['W', 'W', 'B', 'W', 'B', 'W']] 
# 
# N = 3
# 输出: 6
# 解析: 所有粗体的'B'都是我们所求的像素(第1列和第3列的所有'B').
# ⁠       0    1    2    3    4    5
# 列号                                          
# 0    [['W', 'B', 'W', 'B', 'B', 'W'],    
# 1     ['W', 'B', 'W', 'B', 'B', 'W'],    
# 2     ['W', 'B', 'W', 'B', 'B', 'W'],    
# 3     ['W', 'W', 'B', 'W', 'B', 'W']]    
# 行号
# 
# 以R = 0行和C = 1列的'B'为例:
# 规则 1，R = 0行和C = 1列都恰好有N = 3个黑色像素. 
# 规则 2，在C = 1列的黑色像素分别位于0，1和2行。它们都和R = 0行完全相同。
# 
# 
# 
# 
# 
# 注意:
# 
# 
# 输入二维数组行和列的范围是 [1,200]。
# 
# 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findBlackPixel(self, picture: List[List[str]], N: int) -> int:

        cd, rd = {}, {}
        for j in range(len(picture[0])):
            cd[j] = 0

        for i in range(len(picture)):
            r = "".join(picture[i])
            if r not in rd:
                rd[r] = {"r": {i}, "c": set()}
                for j in range(len(r)):
                    if r[j] == "B":
                        rd[r]["c"] |= {j}
                        cd[j] += 1
            else:
                rd[r]["r"] |= {i}
                for j in rd[r]["c"]:
                    cd[j] += 1

        res = 0
        for i in rd:
            if (len(rd[i]["c"]) != N) | (len(rd[i]["r"]) != N):
                continue
            for j in rd[i]["c"]:
                if cd[j] == N:
                    res += N

        return res

# @lc code=end
