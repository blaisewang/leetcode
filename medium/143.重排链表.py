#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (56.31%)
# Likes:    329
# Dislikes: 0
# Total Accepted:    41.2K
# Total Submissions: 72.8K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 示例 1:
# 
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 
# 示例 2:
# 
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
# 
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        e, s, f = head, head, head
        while f and f.next:
            e = s
            s = s.next
            f = f.next.next
        e.next = None

        p, c = None, s
        while c:
            t = c.next
            c.next = p
            p = c
            c = t

        p1, p2 = head, p
        while p1.next and p2.next:
            t1 = p1.next
            p1.next = p2
            t2 = p2.next
            p2.next = t1
            p1 = t1
            p2 = t2
        if not p1.next:
            p1.next = p2

# @lc code=end
