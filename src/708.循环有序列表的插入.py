#
# @lc app=leetcode.cn id=708 lang=python3
#
# [708] 循环有序列表的插入
#
# https://leetcode-cn.com/problems/insert-into-a-sorted-circular-linked-list/description/
#
# algorithms
# Medium (31.97%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    1.2K
# Total Submissions: 3.8K
# Testcase Example:  '[3,4,1]\n2'
#
# 
# 给定循环升序列表中的一个点，写一个函数向这个列表中插入一个新元素，使这个列表仍然是循环升序的。给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。
# 
# 如果有多个满足条件的插入位置，你可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。
# 
# 如果列表为空（给定的节点是 null），你需要创建一个循环有序列表并返回这个点。否则。请返回原先给定的节点。
# 
# 下面的例子可以帮你更好的理解这个问题：
# 
# 
# 
# 
# 
# 在上图中，有一个包含三个元素的循环有序列表，你获得值为 3 的节点的指针，我们需要向表中插入元素 2。
# 
# 
# 
# 
# 
# 
# 新插入的节点应该在 1 和 3 之间，插入之后，整个列表如上图所示，最后返回节点 3。
# 
#


# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        if not head:
            n = Node(insertVal, head)
            n.next = n
            return n
        p, c = head, head.next
        f = False

        while True:
            if p.val <= insertVal <= c.val:
                f = True
            elif p.val > c.val:
                if insertVal > p.val or insertVal < c.val:
                    f = True
            if f:
                p.next = Node(insertVal, c)
                return head
            p, c = c, c.next
            if p == head:
                break
        p.next = Node(insertVal, c)

        return head

# @lc code=end
