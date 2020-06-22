#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#
# https://leetcode-cn.com/problems/jewels-and-stones/description/
#
# algorithms
# Easy (81.18%)
# Likes:    529
# Dislikes: 0
# Total Accepted:    82.2K
# Total Submissions: 99.4K
# Testcase Example:  '"aA"\n"aAAbbbb"'
#
#  给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
# 
# J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。
# 
# 示例 1:
# 
# 输入: J = "aA", S = "aAAbbbb"
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: J = "z", S = "ZZ"
# 输出: 0
# 
# 
# 注意:
# 
# 
# S 和 J 最多含有50个字母。
# J 中的字符不重复。
# 
# 
#


# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(1 for s in S if s in J)

# @lc code=end
