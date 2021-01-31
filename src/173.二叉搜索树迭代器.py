#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#
# https://leetcode-cn.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (75.25%)
# Likes:    320
# Dislikes: 0
# Total Accepted:    36.8K
# Total Submissions: 48.7K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n[[[7,3,15,null,null,9,20]],[],[],[],[],[],[],[],[],[]]'
#
# 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
# 
# 调用 next() 将返回二叉搜索树中的下一个最小的数。
# 
# 
# 
# 示例：
# 
# 
# 
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // 返回 3
# iterator.next();    // 返回 7
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 9
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 15
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 20
# iterator.hasNext(); // 返回 false
# 
# 
# 
# 提示：
# 
# 
# next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
# 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.h = root
        self.s = deque()

        while root:
            self.s.append(root)
            root = root.left

    def next(self) -> int:
        c = self.s.pop()
        n = c.right
        while n:
            self.s.append(n)
            n = n.left

        return c.val

    def hasNext(self) -> bool:
        return len(self.s) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
