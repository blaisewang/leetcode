#
# @lc app=leetcode.cn id=276 lang=python3
#
# [276] 栅栏涂色
#
# https://leetcode-cn.com/problems/paint-fence/description/
#
# algorithms
# Easy (45.34%)
# Likes:    87
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 10.4K
# Testcase Example:  '3\n2'
#
# 有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，每个栅栏柱可以用其中一种颜色进行上色。
# 
# 你需要给所有栅栏柱上色，并且保证其中相邻的栅栏柱 最多连续两个 颜色相同。然后，返回所有有效涂色的方案数。
# 
# 注意:
# n 和 k 均为非负的整数。
# 
# 示例:
# 
# 输入: n = 3，k = 2
# 输出: 6
# 解析: 用 c1 表示颜色 1，c2 表示颜色 2，所有可能的涂色方案有:
# 
# 柱 1    柱 2   柱 3     
# ⁠-----      -----  -----  -----       
# ⁠  1         c1     c1     c2 
# 2         c1     c2     c1 
# 3         c1     c2     c2 
# 4         c2     c1     c1  
# ⁠  5         c2     c1     c2
# 6         c2     c2     c1
# 
# 
#

# @lc code=start
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if not n or not k:
            return 0

        s, d = 0, k
        for i in range(1, n):
            s, d = d, (k - 1) * (s + d)

        return s + d

# @lc code=end
