#
# @lc app=leetcode.cn id=1644 lang=python3
#
# [1644] 二叉树的最近公共祖先 II
#
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/description/
#
# algorithms
# Medium (47.86%)
# Likes:    1
# Dislikes: 0
# Total Accepted:    98
# Total Submissions: 197
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# 给定一棵二叉树的根节点 root，返回给定节点 p 和 q 的最近公共祖先（LCA）节点。如果 p 或 q 之一不存在于该二叉树中，返回
# null。树中的每个节点值都是互不相同的。
# 
# 根据维基百科中对最近公共祖先节点的定义：“两个节点 p 和 q 在二叉树 T 中的最近公共祖先节点是后代节点中既包括 p 又包括 q
# 的最深节点（我们允许一个节点为自身的一个后代节点）”。一个节点 x 的后代节点是节点 x 到某一叶节点间的路径中的节点 y。
# 
# 
# 
# 示例 1:
# 
# 输入： root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出： 3
# 解释： 节点 5 和 1 的共同祖先节点是 3。
# 
# 示例 2:
# 
# 
# 
# 输入： root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出： 5
# 解释： 节点 5 和 4 的共同祖先节点是 5。根据共同祖先节点的定义，一个节点可以是自身的后代节点。
# 
# 示例 3:
# 
# 
# 
# 输入： root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
# 输出： null
# 解释： 节点 10 不存在于树中，所以返回 null。
# 
# 
# 
# 
# 提示:
# 
# 
# 树中节点个数的范围是 [1, 10^4]。
# -10^9 <= Node.val <= 10^9
# 所有节点的值 Node.val 是互不相同的。
# p != q
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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = [None]

        def traverse(node: TreeNode) -> bool:
            if res[0] is not None:
                return True

            if node is None:
                return False

            l, r = traverse(node.left), traverse(node.right)
            if node == p or node == q:
                if l or r and res[0] is None:
                    res[0] = node
            else:
                if l and r and res[0] is None:
                    res[0] = node

            return (node == p or node == q) or l or r

        traverse(root)

        return res[0]

# @lc code=end
