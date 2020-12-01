#
# @lc app=leetcode.cn id=1660 lang=python3
#
# [1660] 纠正二叉树
#
# https://leetcode-cn.com/problems/correct-a-binary-tree/description/
#
# algorithms
# Medium (84.13%)
# Likes:    1
# Dislikes: 0
# Total Accepted:    56
# Total Submissions: 67
# Testcase Example:  '[1,2,3]\n2\n3'
#
# 你有一棵二叉树，这棵二叉树有个小问题，其中有且只有一个无效节点，它的右子节点错误地指向了与其在同一层且在其右侧的一个其他节点。
# 
# 给定一棵这样的问题二叉树的根节点 root ，将该无效节点及其所有子节点移除（除被错误指向的节点外），然后返回新二叉树的根结点。
# 
# 自定义测试用例：
# 
# 测试用例的输入由三行组成：
# 
# 
# TreeNode root
# int fromNode （在 correctBinaryTree 中不可见）
# int toNode （在 correctBinaryTree 中不可见）
# 
# 
# 当以 root 为根的二叉树被解析后，值为 fromNode 的节点 TreeNode 将其右子节点指向值为 toNode 的节点 TreeNode
# 。然后， root 传入 correctBinaryTree 的参数中。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入: root = [1,2,3], fromNode = 2, toNode = 3
# 输出: [1,null,3]
# 解释: 值为 2 的节点是无效的，所以移除之。
# 
# 
# 示例 2:
# 
# 
# 
# 
# 输入: root = [8,3,1,7,null,9,4,2,null,null,null,5,6], fromNode = 7, toNode = 4
# 输出: [8,3,1,null,null,9,4,null,null,5,6]
# 解释: 值为 7 的节点是无效的，所以移除这个节点及其子节点 2。
# 
# 
# 
# 
# 提示:
# 
# 
# 树中节点个数的范围是 [3, 10^4] 。
# -10^9 
# 所有的 Node.val 都是互不相同的。
# fromNode != toNode
# fromNode 和 toNode 将出现在树中的同一层。
# toNode 在 fromNode 的右侧。
# fromNode.right 在测试用例的树中建立后为 null 。
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


class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        f = False
        dummy = TreeNode(0, root)
        q = deque()
        q.append((root, dummy))

        while len(q) > 0:
            s = set()
            l = []
            for _ in range(len(q)):
                n, p = q.popleft()
                l.append((n, p))
                s.add(n)
                if n.left:
                    q.append((n.left, n))
                if n.right:
                    q.append((n.right, n))

            for n, p in l:
                if n.right in s:
                    if p.left == n:
                        p.left = None
                    else:
                        p.right = None

                    f = True
                    break

            if f:
                break

        return dummy.left

# @lc code=end
