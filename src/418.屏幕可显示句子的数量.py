#
# @lc app=leetcode.cn id=418 lang=python3
#
# [418] 屏幕可显示句子的数量
#
# https://leetcode-cn.com/problems/sentence-screen-fitting/description/
#
# algorithms
# Medium (34.20%)
# Likes:    27
# Dislikes: 0
# Total Accepted:    1.1K
# Total Submissions: 3.1K
# Testcase Example:  '["hello","world"]\n2\n8'
#
# 给你一个 rows x cols 的屏幕和一个用 非空 的单词列表组成的句子，请你计算出给定句子可以在屏幕上完整显示的次数。
# 
# 注意：
# 
# 
# 一个单词不能拆分成两行。
# 单词在句子中的顺序必须保持不变。
# 在一行中 的两个连续单词必须用一个空格符分隔。
# 句子中的单词总量不会超过 100。
# 每个单词的长度大于 0 且不会超过 10。
# 1 ≤ rows, cols ≤ 20,000.
# 
# 
# 
# 
# 示例 1：
# 
# 输入：
# rows = 2, cols = 8, 句子 sentence = ["hello", "world"]
# 
# 输出：
# 1
# 
# 解释：
# hello---
# world---
# 
# 字符 '-' 表示屏幕上的一个空白位置。
# 
# 
# 
# 
# 示例 2：
# 
# 输入：
# rows = 3, cols = 6, 句子 sentence = ["a", "bcd", "e"]
# 
# 输出：
# 2
# 
# 解释：
# a-bcd- 
# e-a---
# bcd-e-
# 
# 字符 '-' 表示屏幕上的一个空白位置。
# 
# 
# 
# 
# 示例 3：
# 
# 输入：
# rows = 4, cols = 5, 句子 sentence = ["I", "had", "apple", "pie"]
# 
# 输出：
# 1
# 
# 解释：
# I-had
# apple
# pie-I
# had--
# 
# 字符 '-' 表示屏幕上的一个空白位置。
# 
# 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        tr = rows
        r, i = 0, 0
        sl = len(sentence) - 1 + sum(len(w) for w in sentence)

        while tr:
            c = cols
            while c >= len(sentence[i]):
                if i == 0 and c >= sl:
                    g = (c + 1) // (sl + 1)
                    r += g
                    c -= g * (sl + 1)
                    if c < len(sentence[0]):
                        break

                c -= len(sentence[i]) + 1
                i += 1
                i %= len(sentence)
                if i == 0:
                    r += 1

            tr -= 1
            if i == 0:
                r = int(r * rows / (rows - tr))
                break

        return r

# @lc code=end
