#
# @lc app=leetcode.cn id=1484 lang=python3
#
# [1484] 克隆含随机指针的二叉树
#
# https://leetcode-cn.com/problems/clone-binary-tree-with-random-pointer/description/
#
# algorithms
# Medium (81.10%)
# Likes:    6
# Dislikes: 0
# Total Accepted:    387
# Total Submissions: 475
# Testcase Example:  '[[1,null],null,[4,3],[7,0]]\r'
#
# 给你一个二叉树，树中每个节点都含有一个附加的随机指针，该指针可以指向树中的任何节点或者指向空（null）。
# 
# 请返回该树的 深拷贝 。
# 
# 该树的输入/输出形式与普通二叉树相同，每个节点都用 [val, random_index] 表示：
# 
# 
# val：表示 Node.val 的整数
# random_index：随机指针指向的节点（在输入的树数组中）的下标；如果未指向任何节点，则为 null 。
# 
# 
# 该树以 Node 类的形式给出，而你需要以 NodeCopy 类的形式返回克隆得到的树。NodeCopy 类和Node 类定义一致。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：root = [[1,null],null,[4,3],[7,0]]
# 输出：[[1,null],null,[4,3],[7,0]]
# 解释：初始二叉树为 [1,null,4,7] 。
# 节点 1 的随机指针指向 null，所以表示为 [1, null] 。
# 节点 4 的随机指针指向 7，所以表示为 [4, 3] 其中 3 是树数组中节点 7 对应的下标。
# 节点 7 的随机指针指向 1，所以表示为 [7, 0] 其中 0 是树数组中节点 1 对应的下标。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：root = [[1,4],null,[1,0],null,[1,5],[1,5]]
# 输出：[[1,4],null,[1,0],null,[1,5],[1,5]]
# 解释：节点的随机指针可以指向它自身。
# 
# 
# 示例 3：
# 
# 
# 
# 输入：root = [[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]
# 输出：[[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]
# 
# 
# 示例 4：
# 
# 输入：root = []
# 输出：[]
# 
# 
# 示例 5：
# 
# 输入：root = [[1,null],null,[2,null],null,[1,null]]
# 输出：[[1,null],null,[2,null],null,[1,null]]
# 
# 
# 
# 
# 提示：
# 
# 
# tree 中节点数目范围是 [0, 1000]
# 每个节点的值的范围是 [1, 10^6]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: Node) -> 'NodeCopy':
        if not root:
            return None

        d = {}

        def traverse(n: Node) -> 'NodeCopy':
            if n in d:
                return d[n]
            node = NodeCopy(n.val)
            d[n] = node
            if n.left:
                node.left = traverse(n.left)
            if n.right:
                node.right = traverse(n.right)
            if n.random:
                node.random = traverse(n.random)
            return node

        return traverse(root)

# @lc code=end
