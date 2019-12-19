#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
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
