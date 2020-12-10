#
# @lc app=leetcode.cn id=411 lang=python3
#
# [411] 最短特异单词缩写
#
# https://leetcode-cn.com/problems/minimum-unique-word-abbreviation/description/
#
# algorithms
# Hard (48.35%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    643
# Total Submissions: 1.3K
# Testcase Example:  '"apple"\n["blade"]'
#
# 字符串 "word" 包含以下这些缩写形式：
# 
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# 
# 给一个目标字符串和一个字符串字典，为目标字符串找一个 最短 长度的缩写字符串，同时这个缩写字符串不是字典中其他字符串的缩写形式。
# 
# 缩写形式中每一个 数字 或者字母都被视为长度为 1 。比方说，缩写形式 "a32bc" 的长度为 4 而不是 5 。
# 
# 注意:
# 
# 
# 如果像第二个示例一样有多个有效答案，你可以返回它们中的任意一个。
# 假设目标字符串的长度为 m ，字典中的字符串数目为 n 。你可以假设 m ≤ 21， n ≤ 1000， 且 log2(n) + m ≤ 20.
# 
# 
# 
# 
# 示例:
# 
# "apple", ["blade"] -> "a4" (因为 "5" 或者 "4e" 同时也是 "blade" 的缩写形式，所以它们是无效的缩写)
# 
# "apple", ["plain", "amber", "blade"] -> "1p3" (其他有效的缩写形式还包括 "ap3", "a3e",
# "2p2", "3le", "3l1")。
# 
# 
# 
# 
#

# @lc code=start

from typing import List


class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        n = len(target)
        m = 1 << n
        r, rc = "", float("inf")
        d = [dictionary[i] for i, b in enumerate(map(lambda x: len(x) == n, dictionary)) if b]

        if not d:
            return str(n)

        for i in range(m):
            indices = []
            for j in range(n):
                if i & (1 << j):
                    indices.append(j)

            f = True
            for w in d:
                all_same = True
                for k in indices:
                    if target[k] != w[k]:
                        all_same = False
                        break
                if all_same:
                    f = False
                    break

            if not f:
                continue

            if not indices:
                s, c = str(len(target)), 1
            else:
                s, c = "", 0
                cur = 0
                for i in indices:
                    if i > cur:
                        s += str(i - cur)
                        c += 1
                    s += target[i]
                    c += 1
                    cur = i + 1

                if i < len(target) - 1:
                    s += str(len(target) - i - 1)
                    c += 1

            if c < rc:
                r = s
                rc = c

        return r

# @lc code=end
