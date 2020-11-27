#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (67.07%)
# Likes:    826
# Dislikes: 0
# Total Accepted:    104.2K
# Total Submissions: 155.3K
# Testcase Example:  '[4,2,1,3]'
#
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
# 
# 进阶：
# 
# 
# 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
# 
# 
# 示例 3：
# 
# 
# 输入：head = []
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 5 * 10^4] 内
# -10^5 
# 
# 
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, l, v = head, 0, 1
        while h:
            h, l = h.next, l + 1

        r = ListNode(0)
        r.next = head
        while v < l:
            p, h = r, r.next
            while h:
                h1, i = h, v
                while i and h:
                    h, i = h.next, i - 1

                if i:
                    break

                h2, i = h, v
                while i and h:
                    h, i = h.next, i - 1

                c1, c2 = v, v - i
                while c1 and c2:
                    if h1.val < h2.val:
                        p.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        p.next, h2, c2 = h2, h2.next, c2 - 1
                    p = p.next

                p.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    p, c1, c2 = p.next, c1 - 1, c2 - 1
                p.next = h

            v *= 2

        return r.next

# @lc code=end
