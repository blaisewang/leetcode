#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#
# https://leetcode-cn.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (65.50%)
# Likes:    235
# Dislikes: 0
# Total Accepted:    45.1K
# Total Submissions: 68.9K
# Testcase Example:  '[4,2,1,3]'
#
# 对链表进行插入排序。
# 
# 
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
# 
# 
# 
# 插入排序算法：
# 
# 
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
# 
# 
# 
# 
# 示例 1：
# 
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 
# 
# 示例 2：
# 
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
# 
# 
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        d = ListNode(0)
        d.next = head
        l = head
        c = head.next

        while c:
            if l.val <= c.val:
                l = l.next
            else:
                p = d
                while p.next.val <= c.val:
                    p = p.next
                l.next = c.next
                c.next = p.next
                p.next = c
            c = l.next

        return d.next

# @lc code=end
