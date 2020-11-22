#
# @lc app=leetcode.cn id=1273 lang=python3
#
# [1273] 删除树节点
#
# https://leetcode-cn.com/problems/delete-tree-nodes/description/
#
# algorithms
# Medium (53.13%)
# Likes:    16
# Dislikes: 0
# Total Accepted:    1.2K
# Total Submissions: 2.2K
# Testcase Example:  '7\n[-1,0,0,1,2,2,2]\n[1,-2,4,0,-2,-1,-1]'
#
# 给你一棵以节点 0 为根节点的树，定义如下：
# 
# 
# 节点的总数为 nodes 个；
# 第 i 个节点的值为 value[i] ；
# 第 i 个节点的父节点是 parent[i] 。
# 
# 
# 请你删除节点值之和为 0 的每一棵子树。
# 
# 在完成所有删除之后，返回树中剩余节点的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
# 输出：2
# 
# 
# 示例 2：
# 
# 输入：nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]
# 输出：6
# 
# 
# 示例 3：
# 
# 输入：nodes = 5, parent = [-1,0,1,0,0], value = [-672,441,18,728,378]
# 输出：5
# 
# 
# 示例 4：
# 
# 输入：nodes = 5, parent = [-1,0,0,1,1], value = [-686,-842,616,-739,-746]
# 输出：5
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nodes <= 10^4
# parent.length == nodes
# 0 <= parent[i] <= nodes - 1
# parent[0] == -1 表示节点 0 是树的根。
# value.length == nodes
# -10^5 <= value[i] <= 10^5
# 题目输入数据 保证 是一棵 有效的树 。
# 
# 
#

# @lc code=start
from queue import Queue
from typing import List


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        d = [0] * nodes
        for p in parent:
            if p != -1:
                d[p] += 1

        q = Queue()
        c = [1] * nodes
        for i in range(nodes):
            if d[i] == 0:
                q.put_nowait(i)

        while not q.empty():
            v = q.get_nowait()
            if value[v] == 0:
                c[v] = 0
            u = parent[v]
            if u != -1:
                value[u] += value[v]
                c[u] += c[v]
                d[u] -= 1
                if d[u] == 0:
                    q.put_nowait(u)

        return c[0]

# @lc code=end

