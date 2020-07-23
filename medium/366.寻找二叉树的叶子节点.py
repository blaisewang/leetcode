#
# @lc app=leetcode.cn id=366 lang=python3
#
# [366] 寻找二叉树的叶子节点
#
# https://leetcode-cn.com/problems/find-leaves-of-binary-tree/description/
#
# algorithms
# Medium (73.92%)
# Likes:    50
# Dislikes: 0
# Total Accepted:    1.7K
# Total Submissions: 2.3K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给你一棵二叉树，请按以下要求的顺序收集它的全部节点：
# 
# 
# 依次从左到右，每次收集并删除所有的叶子节点
# 重复如上过程直到整棵树为空
# 
# 
# 
# 
# 示例:
# 
# 输入: [1,2,3,4,5]
# 
# 1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 输出: [[4,5,3],[2],[1]]
# 
# 
# 
# 
# 解释:
# 
# 1. 删除叶子节点 [4,5,3] ，得到如下树结构：
# 
# ⁠         1
# ⁠        / 
# ⁠       2          
# 
# 
# 
# 
# 2. 现在删去叶子节点 [2] ，得到如下树结构：
# 
# ⁠         1          
# 
# 
# 
# 
# 3. 现在删去叶子节点 [1] ，得到空树：
# 
# ⁠         []         
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []

        def traverse(node: TreeNode):
            if node is None:
                return -1
            lh = traverse(node.left)
            rh = traverse(node.right)
            h = max(lh, rh) + 1
            if h == len(res):
                res.append([])
            res[h].append(node.val)
            return h

        traverse(root)
        return res

# @lc code=end
