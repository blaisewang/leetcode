#
# @lc app=leetcode.cn id=1088 lang=python3
#
# [1088] 易混淆数 II
#
# https://leetcode-cn.com/problems/confusing-number-ii/description/
#
# algorithms
# Hard (40.96%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    717
# Total Submissions: 1.8K
# Testcase Example:  '20'
#
# 本题我们会将数字旋转 180° 来生成一个新的数字。
# 
# 比如 0、1、6、8、9 旋转 180° 以后，我们得到的新数字分别为 0、1、9、8、6。
# 
# 2、3、4、5、7 旋转 180° 后，是 无法 得到任何数字的。
# 
# 易混淆数（Confusing Number）指的是一个数字在整体旋转 180° 以后，能够得到一个和原来 不同
# 的数，且新数字的每一位都应该是有效的。（请注意，旋转后得到的新数字可能大于原数字）
# 
# 给出正整数 N，请你返回 1 到 N 之间易混淆数字的数量。
# 
# 
# 
# 示例 1：
# 
# 输入：20
# 输出：6
# 解释：
# 易混淆数为 [6,9,10,16,18,19]。
# 6 转换为 9
# 9 转换为 6
# 10 转换为 01 也就是 1
# 16 转换为 91
# 18 转换为 81
# 19 转换为 61
# 
# 
# 示例 2：
# 
# 输入：100
# 输出：19
# 解释：
# 易混淆数为 [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100]。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 10^9
# 
# 
#


# @lc code=start
class Solution:
    def confusingNumberII(self, N: int) -> int:
        c = 0
        cf = ["0", "1", "6", "8", "9"]
        d = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8"}

        def gen(p: str):
            nonlocal c

            if int(p) <= N:
                if not confuse(p):
                    c += 1
            if int(p) > N:
                return -1

            for idx in cf:
                p = p + idx
                res = gen(p)
                if res == -1:
                    break
                p = p[:-1]

        def confuse(k):
            m = ""
            for idx in k:
                if idx not in d:
                    return False
                m += d[idx]

            return "".join(reversed(k)) == m

        for i in cf[1:]:
            gen(i)

        return c

# @lc code=end
