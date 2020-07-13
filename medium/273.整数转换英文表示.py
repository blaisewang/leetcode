#
# @lc app=leetcode.cn id=273 lang=python3
#
# [273] 整数转换英文表示
#
# https://leetcode-cn.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (27.47%)
# Likes:    85
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 21.8K
# Testcase Example:  "123"
#
# 将非负整数转换为其对应的英文表示。可以保证给定输入小于 2^31 - 1 。
# 
# 示例 1:
# 
# 输入: 123
# 输出: "One Hundred Twenty Three"
# 
# 
# 示例 2:
# 
# 输入: 12345
# 输出: "Twelve Thousand Three Hundred Forty Five"
# 
# 示例 3:
# 
# 输入: 1234567
# 输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# 
# 示例 4:
# 
# 输入: 1234567891
# 输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
# 
#

# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        n2s = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty",
            "Twenty One", "Twenty Two", "Twenty Three", "Twenty Four", "Twenty Five", "Twenty Six", "Twenty Seven", "Twenty Eight", "Twenty Nine", "Thirty",
            "Thirty One", "Thirty Two", "Thirty Three", "Thirty Four", "Thirty Five", "Thirty Six", "Thirty Seven", "Thirty Eight", "Thirty Nine", "Forty",
            "Forty One", "Forty Two", "Forty Three", "Forty Four", "Forty Five", "Forty Six", "Forty Seven", "Forty Eight", "Forty Nine", "Fifty",
            "Fifty One", "Fifty Two", "Fifty Three", "Fifty Four", "Fifty Five", "Fifty Six", "Fifty Seven", "Fifty Eight", "Fifty Nine", "Sixty",
            "Sixty One", "Sixty Two", "Sixty Three", "Sixty Four", "Sixty Five", "Sixty Six", "Sixty Seven", "Sixty Eight", "Sixty Nine", "Seventy",
            "Seventy One", "Seventy Two", "Seventy Three", "Seventy Four", "Seventy Five", "Seventy Six", "Seventy Seven", "Seventy Eight", "Seventy Nine", "Eighty",
            "Eighty One", "Eighty Two", "Eighty Three", "Eighty Four", "Eighty Five", "Eighty Six", "Eighty Seven", "Eighty Eight", "Eighty Nine", "Ninety",
            "Ninety One", "Ninety Two", "Ninety Three", "Ninety Four", "Ninety Five", "Ninety Six", "Ninety Seven", "Ninety Eight", "Ninety Nine"
        ]
        ls = ["", " Thousand ", " Million ", " Billion "]

        r = ""
        i = 0
        while num:
            n = num % 1000
            if n < 100:
                o = n2s[n].strip()
            else:
                o = f"{n2s[n // 100]} Hundred {n2s[n % 100]}".strip()
            if o:
                r = f"{o}{ls[i]}{r}"
            i += 1
            num //= 1000

        return r.strip() if r else "Zero"

# @lc code=end
