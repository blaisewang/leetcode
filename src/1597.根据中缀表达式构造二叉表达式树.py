#
# @lc app=leetcode.cn id=1597 lang=python3
#
# [1597] 根据中缀表达式构造二叉表达式树
#
# https://leetcode-cn.com/problems/build-binary-expression-tree-from-infix-expression/description/
#
# algorithms
# Hard (75.51%)
# Likes:    1
# Dislikes: 0
# Total Accepted:    119
# Total Submissions: 167
# Testcase Example:  '"2-3/(5*2)+1"'
#
# 二叉表达式树^【1】是一种表达算术表达式的二叉树。二叉表达式树中的每一个节点都有零个或两个子节点。 叶节点（有 0
# 个子节点的节点）表示操作数，非叶节点（有 2 个子节点的节点）表示运算符： '+' （加）、 '-' （减）、 '*' （乘）和 '/' （除）。
# 
# 对于每一个非叶节点，对应的 中缀表达式^【2】为 (A o B)，其中 A 是左子树所表达的表达式， B 是右子树所表达的表达式，o 是该节点的运算符。
# 
# 给定一个 中缀表达式 字符串 s，其中包含操作数、上面提到的运算符，以及括号 '(' 与 ')' 。
# 
# 返回一个二叉表达式树，其中的 中序遍历^【3】序列对应表达式 s 。
# 
# 注意，表达式的一般解析顺序适用于 s，即优先解析括号内的表达式，然后解析乘除法，最后解析加减法。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：s = "2-3/(5*2)+1"
# 输出：[+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：s = "3*4-2*5"
# 输出：[-,*,*,3,4,2,5]
# 
# 
# 示例 3:
# 
# 
# 输入：s = "1+2+3+4+5"
# 输出：[+,+,5,+,4,null,null,+,3,null,null,1,2]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 
# s 中包含数字和字符 '+'、 '-'、 '*'、 '/'、 '(' 和 ')' 。
# s 中的操作数有且只有一位数字。
# s 保证是一个有效的表达式。
# 
# 
# 
# 
# 参考资料：
# 
# 
# 二叉表达式树：英语维基百科：Binary Expression Tree
# 中缀表达式：英语维基百科：Infix Notation，百度百科：中缀表达式
# 中序遍历：英语维基百科：Tree Traversal - In-order，百度百科：中序遍历
# 
# 
#


# @lc code=start
# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def expTree(self, s: str) -> Node:
        flag = False
        for c in s:
            if c in ["+", "-", "*", "/"]:
                flag = True
                break

        if not flag:
            return Node(s)

        cnt = 0
        for i in range(len(s) - 1, -1, -1):
            c = s[i]

            if c == ")":
                cnt += 1
            elif c == "(":
                cnt -= 1

            if cnt == 0 and (c == "-" or c == "+"):
                n1, n2 = self.expTree(s[:i]), self.expTree(s[i + 1:])
                root = Node(c, n1, n2)

                return root

        cnt = 0
        for i in range(len(s) - 1, -1, -1):
            c = s[i]

            if c == ")":
                cnt += 1
            elif c == "(":
                cnt -= 1

            if cnt == 0 and (c == "*" or c == "/"):
                n1, n2 = self.expTree(s[:i]), self.expTree(s[i + 1:])
                root = Node(c, n1, n2)
                return root

        return self.expTree(s[1:-1])

# @lc code=end
