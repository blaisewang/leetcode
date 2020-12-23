#
# @lc app=leetcode.cn id=1216 lang=python3
#
# [1216] 验证回文字符串 III
#
# https://leetcode-cn.com/problems/valid-palindrome-iii/description/
#
# algorithms
# Hard (51.06%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    1.1K
# Total Submissions: 2.2K
# Testcase Example:  '"abcdeca"\n2'
#
# 给出一个字符串 s 和一个整数 k，请你帮忙判断这个字符串是不是一个「K 回文」。
# 
# 所谓「K 回文」：如果可以通过从字符串中删去最多 k 个字符将其转换为回文，那么这个字符串就是一个「K 回文」。
# 
# 
# 
# 示例：
# 
# 输入：s = "abcdeca", k = 2
# 输出：true
# 解释：删除字符 “b” 和 “e”。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s 中只含有小写英文字母
# 1 <= k <= s.length
# 
# 
#

# @lc code=start
from functools import lru_cache


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)

        @lru_cache(None)
        def helper(i: int, j: int) -> int:
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return min(helper(i + 1, j), helper(i, j - 1)) + 1

            return 0

        return helper(0, n - 1) <= k

# @lc code=end
