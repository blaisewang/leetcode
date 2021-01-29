#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (51.90%)
# Likes:    651
# Dislikes: 0
# Total Accepted:    98.7K
# Total Submissions: 189.5K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
# 
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        d = ListNode(-1)
        d.next = head
        p = d
        for _ in range(m - 1):
            p = p.next

        b = p.next
        t = b.next
        for _ in range(n - m):
            b.next = t.next
            t.next = p.next
            p.next = t
            t = b.next

        return d.next

# @lc code=end
