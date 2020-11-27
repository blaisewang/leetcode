#
# @lc app=leetcode.cn id=255 lang=python3
#
# [255] 验证前序遍历序列二叉搜索树
#
# https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree/description/
#
# algorithms
# Medium (46.37%)
# Likes:    42
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 4.9K
# Testcase Example:  '[5,2,6,1,3]'
#
# 给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。
# 
# 你可以假定该序列中的数都是不相同的。
# 
# 参考以下这颗二叉搜索树：
# 
# ⁠    5
# ⁠   / \
# ⁠  2   6
# ⁠ / \
# ⁠1   3
# 
# 示例 1：
# 
# 输入: [5,2,6,1,3]
# 输出: false
# 
# 示例 2：
# 
# 输入: [5,2,1,3,6]
# 输出: true
# 
# 进阶挑战：
# 
# 您能否使用恒定的空间复杂度来完成此题？
# 
#

# @lc code=start
from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        s = []
        m = float('-inf')
        for i in range(len(preorder)):
            if preorder[i] < m:
                return False
            while s and preorder[i] > s[-1]:
                m = s.pop()
            s.append(preorder[i])
        return True

# @lc code=end
