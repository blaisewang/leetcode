#
# @lc app=leetcode.cn id=1612 lang=python3
#
# [1612] 检查两棵二叉表达式树是否等价
#
# https://leetcode-cn.com/problems/check-if-two-expression-trees-are-equivalent/description/
#
# algorithms
# Medium (72.32%)
# Likes:    1
# Dislikes: 0
# Total Accepted:    128
# Total Submissions: 177
# Testcase Example:  '[x]\n[x]'
#
# 二叉表达式树是一种表达算术表达式的二叉树。二叉表达式树中的每一个节点都有零个或两个子节点。 叶节点（有 0 个子节点的节点）表示操作数，非叶节点（有 2
# 个子节点的节点）<meta charset="UTF-8">表示运算符。在本题中，我们只考虑 '+' 运算符（即加法）。
# 
# 给定两棵二叉表达式树的根节点 root1 和 root2 。如果两棵二叉表达式树等价，返回 true ，否则返回 false 。
# 
# 当两棵二叉搜索树中的变量取任意值，分别求得的值都相等时，我们称这两棵二叉表达式树是等价的。
# 
# 进阶：当你的答案需同时支持 '-' 运算符（减法）时，你该如何修改你的答案？
# 
# 
# 
# 示例 1:
# 
# 输入： root1 = [x], root2 = [x]
# 输出： true
# 
# 
# 示例 2:
# 
# 
# 
# 输入：root1 = [+,a,+,null,null,b,c], root2 = [+,+,b,c,a]
# 输出：true
# 解释：a + (b + c) == (b + c) + a
# 
# 示例 3:
# 
# 
# 
# 输入： root1 = [+,a,+,null,null,b,c], root2 = [+,+,b,d,a]
# 输出： false
# 解释： a + (b + c) != (b + d) + a
# 
# 
# 
# 
# 提示：
# 
# 
# 两棵树中的节点个数相等，且节点个数为范围 [1, 4999] 内的奇数。
# Node.val 是 '+' 或小写英文字母。
# 给定的树保证是有效的二叉表达式树。
# 
# 
#


# @lc code=start
# Definition for a binary tree node.
class Node:
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkEquivalence(self, root1: Node, root2: Node) -> bool:
        def traverse(root: Node, nodes: list):
            if root.left is None and root.right is None:
                nodes.append(root.val)
                return

            for child in [root.left, root.right]:
                if child:
                    traverse(child, nodes)

        s1, s2 = [], []
        traverse(root1, s1)
        traverse(root2, s2)

        s1.sort()
        s2.sort()

        return len(s1) == len(s2) and s1 == s2

# @lc code=end
