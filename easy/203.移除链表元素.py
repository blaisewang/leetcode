#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (42.86%)
# Likes:    312
# Dislikes: 0
# Total Accepted:    48.1K
# Total Submissions: 111.9K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
# 
# 示例:
# 
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        p = ListNode(None)
        p.next, h = head, p

        while p.next:
            if p.next.val == val:
                p.next = p.next.next
                continue
            p = p.next

        return h.next

# @lc code=end
