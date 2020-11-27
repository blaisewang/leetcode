#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#
# https://leetcode-cn.com/problems/buddy-strings/description/
#
# algorithms
# Easy (27.38%)
# Likes:    90
# Dislikes: 0
# Total Accepted:    13.7K
# Total Submissions: 46.9K
# Testcase Example:  '"ab"\n"ba"'
#
# 给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false
# 。
# 
# 
# 
# 示例 1：
# 
# 输入： A = "ab", B = "ba"
# 输出： true
# 
# 
# 示例 2：
# 
# 输入： A = "ab", B = "ab"
# 输出： false
# 
# 
# 示例 3:
# 
# 输入： A = "aa", B = "aa"
# 输出： true
# 
# 
# 示例 4：
# 
# 输入： A = "aaaaaaabc", B = "aaaaaaacb"
# 输出： true
# 
# 
# 示例 5：
# 
# 输入： A = "", B = "aa"
# 输出： false
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A 和 B 仅由小写字母构成。
# 
# 
#

# @lc code=start
from itertools import zip_longest


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if A == B and len(A) > len(set(A)):
            return True

        s = []
        for x, y in zip_longest(A, B):
            if x != y:
                s.append([x, y])

        if len(s) != 2:
            return False

        if s[0][0] == s[1][1] and s[0][1] == s[1][0]:
            return True

        return False

# @lc code=end
