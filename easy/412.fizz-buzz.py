#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode-cn.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (61.85%)
# Likes:    42
# Dislikes: 0
# Total Accepted:    24.2K
# Total Submissions: 39.1K
# Testcase Example:  '1'
#
# 写一个程序，输出从 1 到 n 数字的字符串表示。
# 
# 1. 如果 n 是3的倍数，输出“Fizz”；
# 
# 2. 如果 n 是5的倍数，输出“Buzz”；
# 
# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
# 
# 示例：
# 
# n = 15,
# 
# 返回:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        r = []
        d = {3: "Fizz", 5: "Buzz"}

        for num in range(1, n + 1):

            r_str = ""

            for key in d.keys():
                if num % key == 0:
                    r_str += d[key]

            if not r_str:
                r_str = str(num)

            r.append(r_str)

        return r

# @lc code=end
