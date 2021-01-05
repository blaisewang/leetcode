#
# @lc app=leetcode.cn id=604 lang=python3
#
# [604] 迭代压缩字符串
#
# https://leetcode-cn.com/problems/design-compressed-string-iterator/description/
#
# algorithms
# Easy (36.57%)
# Likes:    31
# Dislikes: 0
# Total Accepted:    1.6K
# Total Submissions: 4.4K
# Testcase Example:  '["StringIterator","next","next","next","next","next","next","hasNext","next","hasNext"]\n[["L1e2t1C1o1d1e1"],[],[],[],[],[],[],[],[],[]]'
#
# 对于一个压缩字符串，设计一个数据结构，它支持如下两种操作： next 和 hasNext。
# 
# 给定的压缩字符串格式为：每个字母后面紧跟一个正整数，这个整数表示该字母在解压后的字符串里连续出现的次数。
# 
# next() - 如果压缩字符串仍然有字母未被解压，则返回下一个字母，否则返回一个空格。
# hasNext() - 判断是否还有字母仍然没被解压。
# 
# 注意：
# 
# 请记得将你的类在 StringIterator 中 初始化 ，因为静态变量或类变量在多组测试数据中不会被自动清空。更多细节请访问 这里 。
# 
# 示例：
# 
# StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
# 
# iterator.next(); // 返回 'L'
# iterator.next(); // 返回 'e'
# iterator.next(); // 返回 'e'
# iterator.next(); // 返回 't'
# iterator.next(); // 返回 'C'
# iterator.next(); // 返回 'o'
# iterator.next(); // 返回 'd'
# iterator.hasNext(); // 返回 true
# iterator.next(); // 返回 'e'
# iterator.hasNext(); // 返回 false
# iterator.next(); // 返回 ' '
# 
# 
# 
# 
#


# @lc code=start
class StringIterator:

    def __init__(self, compressedString: str):
        self.cs = []

        bucket = list(compressedString)[::-1]
        while bucket:
            if not bucket[-1].isdigit():
                self.cs.append(bucket.pop())
            elif bucket[-1].isdigit() and self.cs[-1].isdigit():
                self.cs[-1] += bucket.pop()
            else:
                self.cs.append(bucket.pop())

    def next(self) -> str:
        if self.hasNext():
            if int(self.cs[1]) > 1:
                self.cs[1] = str(int(self.cs[1]) - 1)
                return self.cs[0]
            elif int(self.cs[1]) == 1:
                next_elem = self.cs[0]
                self.cs = self.cs[2:]
                return next_elem
        else:
            return " "

    def hasNext(self) -> bool:
        return self.cs != []

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
