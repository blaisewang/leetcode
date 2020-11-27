#
# @lc app=leetcode.cn id=1055 lang=python3
#
# [1055] 形成字符串的最短路径
#
# https://leetcode-cn.com/problems/shortest-way-to-form-string/description/
#
# algorithms
# Medium (58.71%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    2.1K
# Total Submissions: 3.6K
# Testcase Example:  '"abc"\n"abcbc"'
#
# 对于任何字符串，我们可以通过删除其中一些字符（也可能不删除）来构造该字符串的子序列。
# 
# 给定源字符串 source 和目标字符串
# target，找出源字符串中能通过串联形成目标字符串的子序列的最小数量。如果无法通过串联源字符串中的子序列来构造目标字符串，则返回 -1。
# 
# 
# 
# 示例 1：
# 
# 输入：source = "abc", target = "abcbc"
# 输出：2
# 解释：目标字符串 "abcbc" 可以由 "abc" 和 "bc" 形成，它们都是源字符串 "abc" 的子序列。
# 
# 
# 示例 2：
# 
# 输入：source = "abc", target = "acdbc"
# 输出：-1
# 解释：由于目标字符串中包含字符 "d"，所以无法由源字符串的子序列构建目标字符串。
# 
# 
# 示例 3：
# 
# 输入：source = "xyz", target = "xzyxz"
# 输出：3
# 解释：目标字符串可以按如下方式构建： "xz" + "y" + "xz"。
# 
# 
# 
# 
# 提示：
# 
# 
# source 和 target 两个字符串都只包含 "a"-"z" 的英文小写字母。
# source 和 target 两个字符串的长度介于 1 和 1000 之间。
# 
# 
#


# @lc code=start
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s = source * len(target)
        r, c = len(s) - 1, len(target) - 1
        while c >= 0 and r >= 0:
            if s[r] == target[c]:
                c -= 1
            r -= 1
        if c >= 0:
            return -1
        return len(target) - (r + 1) // len(source)

# @lc code=end
