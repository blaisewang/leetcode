#
# @lc app=leetcode.cn id=369 lang=python3
#
# [369] 给单链表加一
#
# https://leetcode-cn.com/problems/plus-one-linked-list/description/
#
# algorithms
# Medium (61.50%)
# Likes:    32
# Dislikes: 0
# Total Accepted:    2K
# Total Submissions: 3.3K
# Testcase Example:  '[1,2,3]'
#
# 用一个 非空 单链表来表示一个非负整数，然后将这个整数加一。
# 
# 你可以假设这个整数除了 0 本身，没有任何前导的 0。
# 
# 这个整数的各个数位按照 高位在链表头部、低位在链表尾部 的顺序排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出: [1,2,4]
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
    def plusOne(self, head: ListNode) -> ListNode:
        d = ListNode(0)
        d.next = head
        nn = d

        while head:
            if head.val != 9:
                nn = head
            head = head.next

        nn.val += 1
        nn = nn.next

        while nn:
            nn.val = 0
            nn = nn.next

        return d if d.val else d.next

# @lc code=end
