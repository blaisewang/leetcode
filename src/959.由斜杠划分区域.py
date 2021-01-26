#
# @lc app=leetcode.cn id=959 lang=python3
#
# [959] 由斜杠划分区域
#
# https://leetcode-cn.com/problems/regions-cut-by-slashes/description/
#
# algorithms
# Medium (67.66%)
# Likes:    123
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 6.8K
# Testcase Example:  '[" /","/ "]'
#
# 在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。
# 
# （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。
# 
# 返回区域的数目。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：
# [
# " /",
# "/ "
# ]
# 输出：2
# 解释：2x2 网格如下：
# 
# 
# 示例 2：
# 
# 输入：
# [
# " /",
# "  "
# ]
# 输出：1
# 解释：2x2 网格如下：
# 
# 
# 示例 3：
# 
# 输入：
# [
# "\\/",
# "/\\"
# ]
# 输出：4
# 解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
# 2x2 网格如下：
# 
# 
# 示例 4：
# 
# 输入：
# [
# "/\\",
# "\\/"
# ]
# 输出：5
# 解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
# 2x2 网格如下：
# 
# 
# 示例 5：
# 
# 输入：
# [
# "//",
# "/ "
# ]
# 输出：3
# 解释：2x2 网格如下：
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length == grid[0].length <= 30
# grid[i][j] 是 '/'、'\'、或 ' '。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        up, down, left, right = 0, 1, 2, 3
        relations = {
            " ": {
                up: [(0, 0, down), (0, 0, left), (0, 0, right), (-1, 0, down)],
                down: [(0, 0, up), (0, 0, left), (0, 0, right), (1, 0, up)],
                left: [(0, 0, up), (0, 0, down), (0, 0, right), (0, -1, right)],
                right: [(0, 0, up), (0, 0, down), (0, 0, left), (0, 1, left)],
            },
            "/": {
                up: [(0, 0, left), (-1, 0, down)],
                down: [(0, 0, right), (1, 0, up)],
                left: [(0, 0, up), (0, -1, right)],
                right: [(0, 0, down), (0, 1, left)],
            },
            "\\": {
                up: [(0, 0, right), (-1, 0, down)],
                down: [(0, 0, left), (1, 0, up)],
                left: [(0, 0, down), (0, -1, right)],
                right: [(0, 0, up), (0, 1, left)],
            }
        }

        n = len(grid)
        v = set()
        res = 0

        def bfs(tr: int, tc: int, td: int):
            q = [(tr, tc, td)]
            for x in q:
                tr, tc, td = x
                char = grid[tr][tc]
                for nex in relations[char][td]:
                    dr, dc, dd = nex
                    rr, cc = tr + dr, tc + dc
                    if 0 <= rr < n and 0 <= cc < n and (rr, cc, dd) not in v:
                        q.append((rr, cc, dd))
                        v.add((rr, cc, dd))

        for r in range(n):
            for c in range(n):
                for d in range(4):
                    if (r, c, d) not in v:
                        res += 1
                        bfs(r, c, d)

        return res

# @lc code=end
