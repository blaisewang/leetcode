#
# @lc app=leetcode.cn id=1100 lang=python3
#
# [1100] 长度为 K 的无重复字符子串
#
# https://leetcode-cn.com/problems/find-k-length-substrings-with-no-repeated-characters/description/
#
# algorithms
# Medium (69.68%)
# Likes:    19
# Dislikes: 0
# Total Accepted:    3K
# Total Submissions: 4.3K
# Testcase Example:  '"havefunonleetcode"\n5'
#
# 给你一个字符串 S，找出所有长度为 K 且不含重复字符的子串，请你返回全部满足要求的子串的 数目。
# 
# 
# 
# 示例 1：
# 
# 输入：S = "havefunonleetcode", K = 5
# 输出：6
# 解释：
# 这里有 6 个满足题意的子串，分别是：'havef','avefu','vefun','efuno','etcod','tcode'。
# 
# 
# 示例 2：
# 
# 输入：S = "home", K = 5
# 输出：0
# 解释：
# 注意：K 可能会大于 S 的长度。在这种情况下，就无法找到任何长度为 K 的子串。
# 
# 
# 
# 提示：
# 
# 
# 1 <= S.length <= 10^4
# S 中的所有字符均为小写英文字母
# 1 <= K <= 10^4
# 
# 
#


# @lc code=start
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        r = 0
        for i in range(len(S) - K + 1):
            if len(set(S[i:i + K])) == K:
                r += 1

        return r

# @lc code=end
