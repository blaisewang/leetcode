#
# @lc app=leetcode.cn id=1506 lang=python3
#
# [1506] 找到 N 叉树的根节点
#
# https://leetcode-cn.com/problems/find-root-of-n-ary-tree/description/
#
# algorithms
# Medium (80.49%)
# Likes:    6
# Dislikes: 0
# Total Accepted:    198
# Total Submissions: 246
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一棵 N 叉树 的所有节点在一个数组  Node[] tree 中，树中每个节点都有 唯一的值 。
# 
# 找到并返回 N 叉树的 根节点 。
# 
# 
# 
# 自定义测试：
# 
# N 叉树的输入序列为其层序遍历序列，每组子节点用 null 分隔（见示例）。
# 
# 
# 
# 上图中的 N 叉树的序列化描述为
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# 。
# 
# 测试将以下列方式进行：
# 
# 
# 输入数据的形式为树的序列化描述。
# 驱动程序代码将根据序列化的输入数据构造树，并以任意顺序将每个 Node 对象放入一个数组中。
# 驱动程序代码将把数组传递给 findRoot ，你所编写的函数应该在数组中查找并返回根 Node 对象。
# 驱动程序代码将接受返回的 Node 对象并对其进行序列化。如果序列化的结果和输入数据 相同 ，则测试 通过 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：tree = [1,null,3,2,4,null,5,6]
# 输出：[1,null,3,2,4,null,5,6]
# 解释：来自输入数据的树如上所示。
# 驱动程序代码创建树，并以任意顺序向 findRoot 提供 Node 对象。
# 例如，传递的数组可以是 [Node(5),Node(4),Node(3),Node(6),Node(2),Node(1)] 或
# [Node(2),Node(6),Node(1),Node(3),Node(5),Node(4)] 。
# findRoot 函数应该返回根 Node(1) ，驱动程序代码将序列化它并与输入数据进行比较。
# 输入数据和序列化的 Node(1) 相同，因此测试通过。
# 
# 示例 2：
# 
# 
# 
# 
# 输入：tree =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# 
# 输出：[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# 
# 
# 
# 
# 提示：
# 
# 
# 节点的总个数在 [1, 5*10^4] 之间。
# 每个节点都有唯一的值。
# 
# 
# 
# 
# 进阶：
# 
# 
# 你可以使用 O(1) 额外内存空间且 O(n) 时间复杂度的算法来找到该树的根节点吗？
# 
# 
#

# @lc code=start
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def findRoot(self, tree: List[Node]) -> Node:
        d = dict()

        def get_high(node: Node) -> int:
            if not node:
                return 0

            ch = 0
            for cn in node.children:
                if cn in d:
                    ch = max(ch, d[cn])
                else:
                    ch = max(ch, get_high(cn))
            if node not in d:
                d[node] = ch + 1

            return ch + 1

        ah = 0
        root = None
        for n in tree:
            if n not in d:
                high = get_high(n)
            else:
                high = d[n]
            if high > ah:
                ah = high
                root = n

        return root

# @lc code=end
