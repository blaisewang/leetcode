#
# @lc app=leetcode.cn id=156 lang=python3
#
# [156] 上下翻转二叉树
#
# https://leetcode-cn.com/problems/binary-tree-upside-down/description/
#
# algorithms
# Medium (74.26%)
# Likes:    35
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 3.6K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一个二叉树，其中所有的右节点要么是具有兄弟节点（拥有相同父节点的左节点）的叶节点，要么为空，将此二叉树上下翻转并将它变成一棵树，
# 原来的右节点将转换成左叶节点。返回新的根。
# 
# 例子:
# 
# 输入: [1,2,3,4,5]
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \
# 4   5
# 
# 输出: 返回二叉树的根 [4,5,2,#,#,3,1]
# 
# ⁠  4
# ⁠ / \
# ⁠5   2
# ⁠   / \
# ⁠  3   1  
# 
# 
# 说明:
# 
# 对 [4,5,2,#,#,3,1] 感到困惑? 下面详细介绍请查看 二叉树是如何被序列化的。
# 
# 二叉树的序列化遵循层次遍历规则，当没有节点存在时，'#' 表示路径终止符。
# 
# 这里有一个例子:
# 
# ⁠  1
# ⁠ / \
# ⁠2   3
# ⁠   /
# ⁠  4
# ⁠   \
# ⁠    5
# 
# 
# 上面的二叉树则被序列化为 [1,2,3,#,#,4,#,#,5].
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
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if root is None or root.left is None:
            return root

        nr = self.upsideDownBinaryTree(root.left)
        rr = nr
        while rr.right is not None:
            rr = rr.right

        rr.left = root.right
        rr.right = TreeNode(root.val)
        return nr

# @lc code=end
