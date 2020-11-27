#
# @lc app=leetcode.cn id=663 lang=python3
#
# [663] 均匀树划分
#
# https://leetcode-cn.com/problems/equal-tree-partition/description/
#
# algorithms
# Medium (46.31%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    1.1K
# Total Submissions: 2.4K
# Testcase Example:  '[5,10,10,null,null,2,3]'
#
# 给定一棵有 n 个结点的二叉树，你的任务是检查是否可以通过去掉树上的一条边将树分成两棵，且这两棵树结点之和相等。
# 
# 样例 1:
# 
# 输入:     
# ⁠   5
# ⁠  / \
# ⁠ 10 10
# ⁠   /  \
# ⁠  2   3
# 
# 输出: True
# 解释: 
# ⁠   5
# ⁠  / 
# ⁠ 10
# ⁠     
# 和: 15
# 
# ⁠  10
# ⁠ /  \
# ⁠2    3
# 
# 和: 15
# 
# 
# 
# 
# 样例 2:
# 
# 输入:     
# ⁠   1
# ⁠  / \
# ⁠ 2  10
# ⁠   /  \
# ⁠  2   20
# 
# 输出: False
# 解释: 无法通过移除一条树边将这棵树划分成结点之和相等的两棵子树。
# 
# 
# 
# 
# 注释 :
# 
# 
# 树上结点的权值范围 [-100000, 100000]。
# 1 <= n <= 10000
# 
# 
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
    def checkEqualTree(self, root: TreeNode) -> bool:
        seen = []

        def sum_(node: TreeNode):
            if not node:
                return 0
            seen.append(sum_(node.left) + sum_(node.right) + node.val)
            return seen[-1]

        total = sum_(root)
        seen.pop()
        return total / 2.0 in seen

# @lc code=end
