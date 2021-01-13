#
# @lc app=leetcode.cn id=1202 lang=python3
#
# [1202] 交换字符串中的元素
#
# https://leetcode-cn.com/problems/smallest-string-with-swaps/description/
#
# algorithms
# Medium (34.84%)
# Likes:    80
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 13.8K
# Testcase Example:  '"dcab"\n[[0,3],[1,2]]'
#
# 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0
# 开始）。
# 
# 你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
# 
# 返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
# 
# 
# 
# 示例 1:
# 
# 输入：s = "dcab", pairs = [[0,3],[1,2]]
# 输出："bacd"
# 解释： 
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[1] 和 s[2], s = "bacd"
# 
# 
# 示例 2：
# 
# 输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# 输出："abcd"
# 解释：
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[0] 和 s[2], s = "acbd"
# 交换 s[1] 和 s[2], s = "abcd"
# 
# 示例 3：
# 
# 输入：s = "cba", pairs = [[0,1],[1,2]]
# 输出："abc"
# 解释：
# 交换 s[0] 和 s[1], s = "bca"
# 交换 s[1] 和 s[2], s = "bac"
# 交换 s[0] 和 s[1], s = "abc"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s 中只含有小写英文字母
# 
# 
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        p = {i: i for i in range(len(s))}

        def f(x: int) -> int:
            if x != p[x]:
                p[x] = f(p[x])
            return p[x]

        for i, j in pairs:
            p[f(j)] = f(i)

        d = defaultdict(list)
        for i, j in enumerate(map(f, p)):
            d[j].append(i)

        r = list(s)
        for q in d.values():
            t = sorted(r[i] for i in q)
            for i, c in zip(sorted(q), t):
                r[i] = c

        return "".join(r)

# @lc code=end
