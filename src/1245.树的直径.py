#
# @lc app=leetcode.cn id=1245 lang=python3
#
# [1245] 树的直径
#
# https://leetcode-cn.com/problems/tree-diameter/description/
#
# algorithms
# Medium (47.62%)
# Likes:    51
# Dislikes: 0
# Total Accepted:    2.4K
# Total Submissions: 5K
# Testcase Example:  '[[0,1],[0,2]]'
#
# 给你这棵「无向树」，请你测算并返回它的「直径」：这棵树上最长简单路径的 边数。
# 
# 我们用一个由所有「边」组成的数组 edges 来表示一棵无向树，其中 edges[i] = [u, v] 表示节点 u 和 v 之间的双向边。
# 
# 树上的节点都已经用 {0, 1, ..., edges.length} 中的数做了标记，每个节点上的标记都是独一无二的。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：edges = [[0,1],[0,2]]
# 输出：2
# 解释：
# 这棵树上最长的路径是 1 - 0 - 2，边数为 2。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
# 输出：4
# 解释： 
# 这棵树上最长的路径是 3 - 2 - 1 - 4 - 5，边数为 4。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= edges.length < 10^4
# edges[i][0] != edges[i][1]
# 0 <= edges[i][j] <= edges.length
# edges 会形成一棵无向树
# 
# 
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        r = 0
        visited = [False] * (len(edges) + 1)

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def get_longest_path(index: int):
            nonlocal r

            m1, m2 = 0, 0
            visited[index] = True
            for child in adj[index]:
                if not visited[child]:
                    m = get_longest_path(child)
                    if m > m1:
                        m2 = m1
                        m1 = m
                    elif m > m2:
                        m2 = m

            visited[index] = False
            r = max(r, m1 + m2)

            return max(m1, m2) + 1

        get_longest_path(0)

        return r

# @lc code=end
