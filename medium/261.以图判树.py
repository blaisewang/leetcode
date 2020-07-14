#
# @lc app=leetcode.cn id=261 lang=python3
#
# [261] 以图判树
#
# https://leetcode-cn.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (46.65%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 7.4K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# 给定从 0 到 n-1 标号的 n 个结点，和一个无向边列表（每条边以结点对来表示），请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。
# 
# 示例 1：
# 
# 输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
# 输出: true
# 
# 示例 2:
# 
# 输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# 输出: false
# 
# 注意：你可以假定边列表 edges 中不会出现重复的边。由于所有的边是无向边，边 [0,1] 和边 [1,0] 是相同的，因此不会同时出现在边列表
# edges 中。
# 
#

# @lc code=start
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        g = [i for i in range(n)]

        def find(a):
            if a != g[a]:
                g[a] = find(g[a])
            return g[a]

        def union(a, b):
            g[find(b)] = find(a)

        for edge in edges:
            union(edge[0], edge[1])
        for i in range(n):
            find(i)

        return len(set(g)) == 1

# @lc code=end
