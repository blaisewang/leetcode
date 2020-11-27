#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#
# https://leetcode-cn.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (61.29%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    12.6K
# Total Submissions: 20.1K
# Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n' + '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# 请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
# 
# 
# 
# 举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
# 
# 如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
# 
# 如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
# 
# 
# 
# 提示：
# 
# 
# 给定的两颗树可能会有 1 到 200 个结点。
# 给定的两颗树上的值介于 0 到 200 之间。
# 
# 
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def traverse(node: TreeNode):
            if not node.left and not node.right:
                yield node.val
            if node.left:
                yield from traverse(node.left)
            if node.right:
                yield from traverse(node.right)

        return list(traverse(root1)) == list(traverse(root2))

# @lc code=end
