#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (73.33%)
# Likes:    345
# Dislikes: 0
# Total Accepted:    56.5K
# Total Submissions: 74.3K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
# 
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# 
# 示例:
# 
# 给定的有序链表： [-10, -3, 0, 5, 9],
# 
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getLength(h: ListNode) -> int:
            ret = 0
            while h:
                ret += 1
                h = h.next
            return ret

        def buildTree(l: int, r: int) -> TreeNode:
            if l > r:
                return None
            m = (l + r + 1) // 2
            root = TreeNode()
            root.left = buildTree(l, m - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = buildTree(m + 1, r)
            return root

        return buildTree(0, getLength(head) - 1)

# @lc code=end
