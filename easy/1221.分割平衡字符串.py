#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#
# https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/description/
#
# algorithms
# Easy (76.21%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    19.8K
# Total Submissions: 25.2K
# Testcase Example:  '"RLRRLLRLRL"'
#
# 在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。
# 
# 给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
# 
# 返回可以通过分割得到的平衡字符串的最大数量。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "RLRRLLRLRL"
# 输出：4
# 解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
# 
# 
# 示例 2：
# 
# 输入：s = "RLLLLRRRLR"
# 输出：3
# 解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。
# 
# 
# 示例 3：
# 
# 输入：s = "LLLLRRRR"
# 输出：1
# 解释：s 只能保持原样 "LLLLRRRR".
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s[i] = 'L' 或 'R'
# 分割得到的每个字符串都必须是平衡字符串。
# 
# 
#


# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if s[0] == "L":
            t = [1]
        else:
            t = [-1]
        for i in range(1, len(s)):
            if s[i] == "L":
                t.append(t[-1] + 1)
            else:
                t.append(t[-1] - 1)
        return t.count(0)

# @lc code=end
