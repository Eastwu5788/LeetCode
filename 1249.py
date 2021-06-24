# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2021
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '6/24/21 1:57 PM'
"""
给你一个由 '('、')' 和小写字母组成的字符串 s。

你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。

请返回任意一个合法字符串。

有效「括号字符串」应当符合以下 任意一条 要求：

空字符串或只包含小写字母的字符串
可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」
"""


class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        left_stack = list()
        s = list(s)

        for idx, char in enumerate(s):
            if char == "(":
                left_stack.append(idx)

            if char == ")":
                # 匹配到了一个括号对
                if len(left_stack) > 0:
                    left_stack.pop()

                else:
                    s[idx] = ""

        while left_stack:
            s[left_stack.pop()] = ""

        return "".join(s)


if __name__ == "__main__":
    print(Solution().minRemoveToMakeValid("))(("))
    print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
    print(Solution().minRemoveToMakeValid("a)b(c)d"))
    print(Solution().minRemoveToMakeValid("(a(b(c)d)"))
