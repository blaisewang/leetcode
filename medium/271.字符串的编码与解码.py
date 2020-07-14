#
# @lc app=leetcode.cn id=271 lang=python3
#
# [271] 字符串的编码与解码
#
# https://leetcode-cn.com/problems/encode-and-decode-strings/description/
#
# algorithms
# Medium (52.93%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    1.3K
# Total Submissions: 2.4K
# Testcase Example:  '["Hello","World"]'
#
# 请你设计一个算法，可以将一个 字符串列表 编码成为一个
# 字符串。这个编码后的字符串是可以通过网络进行高效传送的，并且可以在接收端被解码回原来的字符串列表。
# 
# 1 号机（发送方）有如下函数：
# 
# string encode(vector<string> strs) {
# ⁠ // ... your code
# ⁠ return encoded_string;
# }
# 
# 2 号机（接收方）有如下函数：
# 
# vector<string> decode(string s) {
# ⁠ //... your code
# ⁠ return strs;
# }
# 
# 
# 1 号机（发送方）执行：
# 
# string encoded_string = encode(strs);
# 
# 
# 2 号机（接收方）执行：
# 
# vector<string> strs2 = decode(encoded_string);
# 
# 
# 此时，2 号机（接收方）的 strs2 需要和 1 号机（发送方）的 strs 相同。
# 
# 请你来实现这个 encode 和 decode 方法。
# 
# 注意：
# 
# 
# 因为字符串可能会包含 256 个合法 ascii 字符中的任何字符，所以您的算法必须要能够处理任何可能会出现的字符。
# 请勿使用 “类成员”、“全局变量” 或 “静态变量” 来存储这些状态，您的编码和解码算法应该是非状态依赖的。
# 请不要依赖任何方法库，例如 eval 又或者是 serialize 之类的方法。本题的宗旨是需要您自己实现 “编码” 和 “解码” 算法。
# 
# 
#

# @lc code=start
class Codec:

    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        """
        return "".join([chr(len(x) >> (i * 8) & 0xff) for i in range(4)][::-1])

    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "".join(self.len_to_str(x) + x for x in strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        i, n = 0, len(s)
        o = []
        while i < n:
            l = 0
            for ch in s[i: i + 4]:
                l = l * 256 + ord(ch)
            i += 4
            o.append(s[i: i + l])
            i += l
        return o

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @lc code=end
