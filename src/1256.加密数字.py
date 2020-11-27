#
# @lc app=leetcode.cn id=1256 lang=python3
#
# [1256] 加密数字
#
# https://leetcode-cn.com/problems/encode-number/description/
#
# algorithms
# Medium (63.51%)
# Likes:    13
# Dislikes: 0
# Total Accepted:    1.2K
# Total Submissions: 2K
# Testcase Example:  '23'
#
# 给你一个非负整数 num ，返回它的「加密字符串」。
# 
# 加密的过程是把一个整数用某个未知函数进行转化，你需要从下表推测出该转化函数：
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：num = 23
# 输出："1000"
# 
# 
# 示例 2：
# 
# 输入：num = 107
# 输出："101100"
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= num <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def encode(self, num: int) -> str:
        return bin(num + 1)[3:]

# @lc code=end
