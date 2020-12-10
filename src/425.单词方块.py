#
# @lc app=leetcode.cn id=425 lang=python3
#
# [425] 单词方块
#
# https://leetcode-cn.com/problems/word-squares/description/
#
# algorithms
# Hard (58.51%)
# Likes:    44
# Dislikes: 0
# Total Accepted:    918
# Total Submissions: 1.6K
# Testcase Example:  '["area","lead","wall","lady","ball"]'
#
# 给定一个单词集合 （没有重复），找出其中所有的 单词方块 。
# 
# 一个单词序列形成了一个有效的单词方块的意思是指从第 k 行和第 k 列 (0 ≤ k < max(行数, 列数)) 来看都是相同的字符串。
# 
# 例如，单词序列 ["ball","area","lead","lady"] 形成了一个单词方块，因为每个单词从水平方向看和从竖直方向看都是相同的。
# 
# b a l l
# a r e a
# l e a d
# l a d y
# 
# 
# 注意：
# 
# 
# 单词个数大于等于 1 且不超过 500。
# 所有的单词长度都相同。
# 单词长度大于等于 1 且不超过 5。
# 每个单词只包含小写英文字母 a-z。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：
# ["area","lead","wall","lady","ball"]
# 
# 输出：
# [
# ⁠ [ "wall",
# ⁠   "area",
# ⁠   "lead",
# ⁠   "lady"
# ⁠ ],
# ⁠ [ "ball",
# ⁠   "area",
# ⁠   "lead",
# ⁠   "lady"
# ⁠ ]
# ]
# 
# 解释：
# 输出包含两个单词方块，输出的顺序不重要，只需要保证每个单词方块内的单词顺序正确即可。 
# 
# 
# 
# 
# 示例 2：
# 
# 输入：
# ["abat","baba","atan","atal"]
# 
# 输出：
# [
# ⁠ [ "baba",
# ⁠   "abat",
# ⁠   "baba",
# ⁠   "atan"
# ⁠ ],
# ⁠ [ "baba",
# ⁠   "abat",
# ⁠   "baba",
# ⁠   "atal"
# ⁠ ]
# ]
# 
# 解释：
# 输出包含两个单词方块，输出的顺序不重要，只需要保证每个单词方块内的单词顺序正确即可。 
# 
# 
# 
# 
#

# @lc code=start
from typing import List, Dict


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        d = {}
        r = []
        for word in words:
            c = d
            for w in word:
                c.setdefault(w, {})
                c = c[w]
            c["#"] = "#"

        def helper(prefix: str, l: int) -> List[str]:
            ans = []
            cur = d
            for p in prefix:
                if p not in cur:
                    return ans
                cur = cur[p]

            def dfs(pf: str, cu: Dict):
                if "#" in cu and len(pf) == l:
                    ans.append(pf)
                    return
                if len(pf) > l:
                    return

                for b in cu:
                    if b != "#":
                        dfs(pf + b, cu[b])

            dfs(prefix, cur)
            return ans

        def backtrack(tmp: List[str], l: int):
            tl = len(tmp)
            if tl == l:
                r.append(tmp)
                return

            prefix = ""
            for t in tmp:
                prefix += t[tl]
            for nxt in helper(prefix, l):
                backtrack(tmp + [nxt], l)

        for word in words:
            backtrack([word], len(word))

        return r

# @lc code=end
