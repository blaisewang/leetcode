#
# @lc app=leetcode.cn id=422 lang=python3
#
# [422] 有效的单词方块
#
# https://leetcode-cn.com/problems/valid-word-square/description/
#
# algorithms
# Easy (41.70%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    1.3K
# Total Submissions: 3.1K
# Testcase Example:  '["abcd","bnrt","crmy","dtye"]'
#
# 给你一个单词序列，判断其是否形成了一个有效的单词方块。
# 
# 有效的单词方块是指此由单词序列组成的文字方块的 第 k 行 和 第 k 列 (0 ≤ k < max(行数, 列数)) 所显示的字符串完全相同。
# 
# 注意：
# 
# 
# 给定的单词数大于等于 1 且不超过 500。
# 单词长度大于等于 1 且不超过 500。
# 每个单词只包含小写英文字母 a-z。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：
# [
# ⁠ "abcd",
# ⁠ "bnrt",
# ⁠ "crmy",
# ⁠ "dtye"
# ]
# 
# 输出：
# true
# 
# 解释：
# 第 1 行和第 1 列都是 "abcd"。
# 第 2 行和第 2 列都是 "bnrt"。
# 第 3 行和第 3 列都是 "crmy"。
# 第 4 行和第 4 列都是 "dtye"。
# 
# 因此，这是一个有效的单词方块。
# 
# 
# 
# 
# 示例 2：
# 
# 输入：
# [
# ⁠ "abcd",
# ⁠ "bnrt",
# ⁠ "crm",
# ⁠ "dt"
# ]
# 
# 输出：
# true
# 
# 解释：
# 第 1 行和第 1 列都是 "abcd"。
# 第 2 行和第 2 列都是 "bnrt"。
# 第 3 行和第 3 列都是 "crm"。
# 第 4 行和第 4 列都是 "dt"。
# 
# 因此，这是一个有效的单词方块。
# 
# 
# 
# 
# 示例 3：
# 
# 输入：
# [
# ⁠ "ball",
# ⁠ "area",
# ⁠ "read",
# ⁠ "lady"
# ]
# 
# 输出：
# false
# 
# 解释：
# 第 3 行是 "read" ，然而第 3 列是 "lead"。
# 
# 因此，这 不是 一个有效的单词方块。
# 
# 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        ml = max([len(x) for x in words])

        for i in range(len(words)):
            words[i] = words[i].ljust(ml, "0")
        for i in range(len(words), ml):
            words.append("0" * ml)

        return words == list(map(lambda x: "".join(x), list(zip(*words))))

# @lc code=end
