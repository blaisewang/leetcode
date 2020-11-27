#
# @lc app=leetcode.cn id=1062 lang=python3
#
# [1062] 最长重复子串
#
# https://leetcode-cn.com/problems/longest-repeating-substring/description/
#
# algorithms
# Medium (50.24%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 4.4K
# Testcase Example:  '"abcd"'
#
# 给定字符串 S，找出最长重复子串的长度。如果不存在重复子串就返回 0。
# 
# 
# 
# 示例 1：
# 
# 输入："abcd"
# 输出：0
# 解释：没有重复子串。
# 
# 
# 示例 2：
# 
# 输入："abbaba"
# 输出：2
# 解释：最长的重复子串为 "ab" 和 "ba"，每个出现 2 次。
# 
# 
# 示例 3：
# 
# 输入："aabcaabdaab"
# 输出：3
# 解释：最长的重复子串为 "aab"，出现 3 次。
# 
# 
# 示例 4：
# 
# 输入："aaaaa"
# 输出：4
# 解释：最长的重复子串为 "aaaa"，出现 2 次。
# 
# 
# 
# 提示：
# 
# 
# 字符串 S 仅包含从 'a' 到 'z' 的小写英文字母。
# 1 <= S.length <= 1500
# 
# 
#

# @lc code=start


class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:

        def search(L: int) -> int:
            a, h = 26, 0
            mods = 2 ** 24
            numbers = [ord(S[i]) - ord("a") for i in range(len(S))]

            for i in range(L):
                h = (h * a + numbers[i]) % mods

            seen = {h}
            aL = pow(a, L, mods)
            for start in range(1, len(S) - L + 1):
                h = (h * a - numbers[start - 1] * aL + numbers[start + L - 1]) % mods
                if h in seen:
                    return start
                seen.add(h)
            return -1

        l, r = 1, len(S)
        while l <= r:
            L = l + (r - l) // 2
            if search(L) != -1:
                l = L + 1
            else:
                r = L - 1

        return l - 1

# @lc code=end
