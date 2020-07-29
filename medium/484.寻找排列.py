#
# @lc app=leetcode.cn id=484 lang=python3
#
# [484] 寻找排列
#
# https://leetcode-cn.com/problems/find-permutation/description/
#
# algorithms
# Medium (65.58%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    787
# Total Submissions: 1.2K
# Testcase Example:  '"DDIIDI"'
#
# 现在给定一个只由字符 'D' 和 'I' 组成的 秘密签名。'D' 表示两个数字间的递减关系，'I' 表示两个数字间的递增关系。并且 秘密签名
# 是由一个特定的整数数组生成的，该数组唯一地包含 1 到 n 中所有不同的数字（秘密签名的长度加 1 等于 n）。例如，秘密签名 "DI" 可以由数组
# [2,1,3] 或 [3,1,2] 生成，但是不能由数组 [3,2,4] 或 [2,1,3,4] 生成，因为它们都不是合法的能代表 "DI" 秘密签名
# 的特定串。
# 
# 现在你的任务是找到具有最小字典序的 [1, 2, ... n] 的排列，使其能代表输入的 秘密签名。
# 
# 示例 1：
# 
# 输入： "I"
# 输出： [1,2]
# 解释： [1,2] 是唯一合法的可以生成秘密签名 "I" 的特定串，数字 1 和 2 构成递增关系。
# 
# 
# 
# 
# 示例 2：
# 
# 输入： "DI"
# 输出： [2,1,3]
# 解释： [2,1,3] 和 [3,1,2] 可以生成秘密签名 "DI"，
# 但是由于我们要找字典序最小的排列，因此你需要输出 [2,1,3]。
# 
# 
# 
# 
# 注：
# 
# 
# 输出字符串只会包含字符 'D' 和 'I'。
# 输入字符串的长度是一个正整数且不会超过 10,000。
# 
# 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        if not s:
            return [1]

        r, a = [1], 0
        for i in range(len(s)):
            if s[i:i + 1] == "D":
                r.insert(a, i + 2)
            else:
                r.append(i + 2)
                a = i + 1

        return r

# @lc code=end
