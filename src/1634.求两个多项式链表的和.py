#
# @lc app=leetcode.cn id=1634 lang=python3
#
# [1634] 求两个多项式链表的和
#
# https://leetcode-cn.com/problems/add-two-polynomials-represented-as-linked-lists/description/
#
# algorithms
# Medium (57.76%)
# Likes:    0
# Dislikes: 0
# Total Accepted:    68
# Total Submissions: 118
# Testcase Example:  '[[1,1]]\n[[1,0]]'
#
# 多项式链表是一种特殊形式的链表，每个节点表示多项式的一项。
# 
# 每个节点有三个属性：
# 
# 
# coefficient：该项的系数。项 9x^4 的系数是 9 。
# power：该项的指数。项 9x^4 的指数是 4 。
# next：指向下一个节点的指针（引用），如果当前节点为链表的最后一个节点则为 null 。
# 
# 
# 例如，多项式 5x^3 + 4x - 7 可以表示成如下图所示的多项式链表：
# 
# 
# 
# 多项式链表必须是标准形式的，即多项式必须 严格 按指数 power 的递减顺序排列（即降幂排列）。另外，系数 coefficient 为 0
# 的项需要省略。
# 
# 给定两个多项式链表的头节点 poly1 和 poly2，返回它们的和的头节点。
# 
# PolyNode 格式：
# 
# 输入/输出格式表示为 n 个节点的列表，其中每个节点表示为 [coefficient, power] 。例如，多项式 5x^3 + 4x - 7 表示为：
# [[5,3],[4,1],[-7,0]] 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：poly1 = [[1,1]], poly2 = [[1,0]]
# 输出：[[1,1],[1,0]]
# 解释：poly1 = x. poly2 = 1. 和为 x + 1.
# 
# 
# 示例 2：
# 
# 
# 输入：poly1 = [[2,2],[4,1],[3,0]], poly2 = [[3,2],[-4,1],[-1,0]]
# 输出：[[5,2],[2,0]]
# 解释：poly1 = 2x^2 + 4x + 3. poly2 = 3x^2 - 4x - 1. 和为 5x^2 + 2. 注意，我们省略 "0x"
# 项。
# 
# 
# 示例 3：
# 
# 
# 输入：poly1 = [[1,2]], poly2 = [[-1,2]]
# 输出：[]
# 解释：和为 0。我们返回空链表。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^9 
# PolyNode.coefficient != 0
# 0 
# PolyNode.power > PolyNode.next.power
# 
# 
#


# @lc code=start
# Definition for polynomial singly-linked list.
class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next


class Solution:
    def addPoly(self, poly1: PolyNode, poly2: PolyNode) -> PolyNode:
        dummy = PolyNode()
        tail = dummy
        while poly1 or poly2:
            if (poly1 and not poly2) or (poly1 and poly2 and poly1.power > poly2.power):
                tail.next = PolyNode(poly1.coefficient, poly1.power)
                tail = tail.next
                poly1 = poly1.next
                continue

            if (poly2 and not poly1) or (poly1 and poly2 and poly2.power > poly1.power):
                tail.next = PolyNode(poly2.coefficient, poly2.power)
                tail = tail.next
                poly2 = poly2.next
                continue

            if poly1.coefficient + poly2.coefficient != 0:
                tail.next = PolyNode(poly1.coefficient + poly2.coefficient, poly1.power)
                tail = tail.next

            poly1, poly2 = poly1.next, poly2.next

        return dummy.next

# @lc code=end
