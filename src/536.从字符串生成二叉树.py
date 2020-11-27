#
# @lc app=leetcode.cn id=536 lang=python3
#
# [536] 从字符串生成二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-string/description/
#
# algorithms
# Medium (52.24%)
# Likes:    38
# Dislikes: 0
# Total Accepted:    1.9K
# Total Submissions: 3.6K
# Testcase Example:  '"4(2(3)(1))(6(5))"'
#
# 你需要从一个包括括号和整数的字符串构建一棵二叉树。
# 
# 输入的字符串代表一棵二叉树。它包括整数和随后的 0 ，1 或 2 对括号。整数代表根的值，一对括号内表示同样结构的子树。
# 
# 若存在左子结点，则从左子结点开始构建。
# 
# 
# 
# 示例：
# 
# 输入："4(2(3)(1))(6(5))"
# 输出：返回代表下列二叉树的根节点:
# 
# ⁠      4
# ⁠    /   \
# ⁠   2     6
# ⁠  / \   / 
# ⁠ 3   1 5   
# 
# 
# 
# 
# 提示：
# 
# 
# 输入字符串中只包含 '(', ')', '-' 和 '0' ~ '9' 
# 空树由 "" 而非"()"表示。
# 
# 
# 
# 
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if s == "":
            return None

        def insert_node(num: int, stack: list) -> tuple:
            node = TreeNode(num)
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            return None, 1, node

        n, f, stk = None, 1, []
        for c in s:
            if c == "(":
                if n is not None:
                    n, f, nd = insert_node(n, stk)
                    stk.append(nd)
            elif c == ")":
                if n is not None:
                    n, f, nd = insert_node(n, stk)
                else:
                    stk.pop()
            elif c == "-":
                f = -1
            else:
                n = (n * 10 + f * int(c)) if n else f * int(c)

        return stk[-1] if stk else TreeNode(n)

# @lc code=end
