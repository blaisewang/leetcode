#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (39.15%)
# Likes:    320
# Dislikes: 0
# Total Accepted:    49.8K
# Total Submissions: 126.8K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
# 
# 示例 1:
# 
# 输入: 1->2
# 输出: false
# 
# 示例 2:
# 
# 输入: 1->2->2->1
# 输出: true
# 
# 
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        fast = slow = head

        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        if fast:
            slow = slow.next

        p, c = None, slow

        while c:
            t = c.next
            c.next = p
            p, c = c, t

        while p and head:

            if p.val != head.val:
                return False
            p, head = p.next, head.next

        return True

# @lc code=end
