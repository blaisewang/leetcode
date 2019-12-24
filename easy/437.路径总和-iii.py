#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        s = [(root, [root.val])]
        r = 0

        while s:
            node, t = s.pop()
            r += t.count(sum)
            t += [0]
            
            if node.left:
                arr = [i + node.left.val for i in t]
                s.append((node.left, arr))

            if node.right:
                arr = [i + node.right.val for i in t]
                s.append((node.right, arr))

        return r

# @lc code=end
