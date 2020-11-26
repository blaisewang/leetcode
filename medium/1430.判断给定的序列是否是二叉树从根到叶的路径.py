#
# @lc app=leetcode.cn id=1430 lang=python3
#
# [1430] 判断给定的序列是否是二叉树从根到叶的路径
#
# https://leetcode-cn.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/description/
#
# algorithms
# Medium (57.98%)
# Likes:    4
# Dislikes: 0
# Total Accepted:    326
# Total Submissions: 558
# Testcase Example:  '[0,1,0,0,1,0,null,null,1,0,0]\n[0,1,0,1]'
#
# 给定一个二叉树，我们称从根节点到任意叶节点的任意路径中的节点值所构成的序列为该二叉树的一个 “有效序列” 。检查一个给定的序列是否是给定二叉树的一个
# “有效序列” 。
# 
# 我们以整数数组 arr 的形式给出这个序列。从根节点到任意叶节点的任意路径中的节点值所构成的序列都是这个二叉树的 “有效序列” 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
# 输出：true
# 解释：
# 路径 0 -> 1 -> 0 -> 1 是一个“有效序列”（图中的绿色节点）。
# 其他的“有效序列”是：
# 0 -> 1 -> 1 -> 0 
# 0 -> 0 -> 0
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
# 输出：false 
# 解释：路径 0 -> 0 -> 1 不存在，所以这不是一个“序列”。
# 
# 
# 示例 3：
# 
# 
# 
# 
# 输入：root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
# 输出：false
# 解释：路径 0 -> 1 -> 1 是一个序列，但不是一个“有效序列”（译者注：因为序列的终点不是叶节点）。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 5000
# 0 <= arr[i] <= 9
# 每个节点的值的取值范围是 [0 - 9]
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
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root:
            if arr:
                return False
            return True

        def traverse(node: TreeNode, a: List[int]) -> bool:
            if not a:
                return False
            if node.val != a[0]:
                return False
            if node.left:
                if traverse(node.left, a[1:]):
                    return True
            if node.right:
                if traverse(node.right, a[1:]):
                    return True
            if not node.left and not node.right:
                if not a[1:]:
                    return True
                return False

        return traverse(root, arr)

# @lc code=end
