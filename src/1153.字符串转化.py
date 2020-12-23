#
# @lc app=leetcode.cn id=1153 lang=python3
#
# [1153] 字符串转化
#
# https://leetcode-cn.com/problems/string-transforms-into-another-string/description/
#
# algorithms
# Hard (35.53%)
# Likes:    44
# Dislikes: 0
# Total Accepted:    1.2K
# Total Submissions: 3.5K
# Testcase Example:  '"aabcc"\n"ccdee"'
#
# 给出两个长度相同的字符串，分别是 str1 和 str2。请你帮忙判断字符串 str1 能不能在 零次 或 多次 转化后变成字符串 str2。
# 
# 每一次转化时，将会一次性将 str1 中出现的 所有 相同字母变成其他 任何 小写英文字母（见示例）。
# 
# 只有在字符串 str1 能够通过上述方式顺利转化为字符串 str2 时才能返回 True，否则返回 False。​​
# 
# 
# 
# 示例 1：
# 
# 输入：str1 = "aabcc", str2 = "ccdee"
# 输出：true
# 解释：将 'c' 变成 'e'，然后把 'b' 变成 'd'，接着再把 'a' 变成 'c'。注意，转化的顺序也很重要。
# 
# 
# 示例 2：
# 
# 输入：str1 = "leetcode", str2 = "codeleet"
# 输出：false
# 解释：我们没有办法能够把 str1 转化为 str2。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= str1.length == str2.length <= 10^4
# str1 和 str2 中都只会出现 小写英文字母
# 
# 
#


# @lc code=start
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        if len(set(str2)) == 26:
            return False

        d = {}
        for i in range(len(str1)):
            d.setdefault(str1[i], []).append(i)

        for idx in d.values():
            for i in idx:
                if str2[i] != str2[idx[0]]:
                    return False

        return True

# @lc code=end
