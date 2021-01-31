#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
# https://leetcode-cn.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (45.91%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    27.9K
# Total Submissions: 60.3K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA
# 中的重复序列有时会对研究非常有帮助。
# 
# 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
# 
# 
# 示例 2：
# 
# 
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# s[i] 为 'A'、'C'、'G' 或 'T'
# 
# 
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = Counter(s[i: i + 10] for i in range(len(s) - 9))
        return list(filter(lambda i: d[i] > 1, d))

# @lc code=end
