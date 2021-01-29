#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (69.23%)
# Likes:    978
# Dislikes: 0
# Total Accepted:    101.8K
# Total Submissions: 147K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
# 
# 示例:
# 
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        c = 1
        for i in range(0, n):
            c = c * 2 * (2 * i + 1) / (i + 2)
        return int(c)

# @lc code=end
