#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (53.24%)
# Likes:    339
# Dislikes: 0
# Total Accepted:    58.8K
# Total Submissions: 110.3K
# Testcase Example:  '1'
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
# 
# 注意：整数顺序将表示为一个字符串。
# 
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "1"
# 
# 
# 示例 2:
# 
# 输入: 4
# 输出: "1211"
# 
# 
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:

        count_l = ["1"]
        for _ in range(n - 1):
            last = count_l[-1]
            current = ""

            count = 0
            current_c = last[0]

            for c in last:
                if c == current_c:
                    count += 1
                else:
                    current += str(count) + current_c
                    current_c = c
                    count = 1

            current += str(count) + current_c

            count_l.append(current)

        return count_l[-1]

# @lc code=end
